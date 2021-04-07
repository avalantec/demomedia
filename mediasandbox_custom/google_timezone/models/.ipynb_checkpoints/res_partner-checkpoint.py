# -*- coding: utf-8 -*-

from odoo import models, fields, api
import requests
import urllib
import time

import logging
log = logging.getLogger(__name__)

#1616457955

class Partner(models.Model):
    _inherit = "res.partner"
    _description = 'Res Partner Inherit'
    
    timezone_name = fields.Char("Timezone Name")
    city_geolocation = fields.Char("City Geolocation")
    
    @api.onchange('country_id', 'zip')
    def _onchange_country_zip(self):
        #1616458033

        self.write({ 'tz':"" })
        
        if self.zip:
            base_url = "https://maps.googleapis.com/maps/api/geocode/json?"

            google_key = self.get_current_google_key()

            if not self.country_id.name:
                usa_country_id = self.env['res.country'].search([ ('name','=', 'United States') ])
                self.write({
                    'country_id': usa_country_id.id,
                })
                
            country = self.country_id.name

            zip_code = self.zip
            params = {
                'address': "{}, {}".format( zip_code, country ),
                'key': google_key
            }
            r= requests.get(base_url, params)
            if r.status_code == 200:
                #1616458058
                r_json = r.json()
                
                if r_json.get("status") == "ZERO_RESULTS":
                    self.write({
                        'city':'No city found',
                        'state_id': "",
                        'city_geolocation': "",
                        'timezone_name': "",
                    })
                    return

                if r_json.get("status") == "OK":
                    results_json = r_json.get("results")[0]
                
                    if not results_json:
                        log.info("Google Timezone: Key Status - Not Found in JSON")
                    else:
                        g_address_components = results_json.get('address_components')

                        g_geolocation = results_json.get('geometry').get('location')
                        
                        g_city = ""
                        g_state_code = ""

                        for record in g_address_components:
                            get_city = self.get_city( record )
                            if get_city:  
                                g_city = get_city

                            get_state_code = self.get_state_code( record )
                            if get_state_code:
                                g_state_code = get_state_code

                            get_country_code = self.get_country_code( record )
                            if get_country_code:
                                g_country_code = get_country_code

                        log.info("===city, state, country = %s %s %s", g_city, g_state_code, g_country_code )
                                
                        if not self.same_country_code(g_country_code):
                            self.write( {
                                'city': "No City Found",
                                'state_id': "",
                                'city_geolocation': "",
                                'timezone_name': "",
                                
                            })
                            return
                        
                        if g_city:
                            self.write({ 'city': g_city })
                            
                        if g_geolocation:
                            latitude = "{:+.5f}".format( g_geolocation.get("lat") )
                            longitude = "{:+.5f}".format( g_geolocation.get("lng") )
                            self.write({ 'city_geolocation': latitude + "," + longitude })
                        
                        if g_country_code and g_state_code:
                            o_state_id = self.odoo_get_state_id( g_country_code, g_state_code )
                            self.write({ 'state_id': o_state_id })
            return

    def get_city(self, record):
        #1616458059
        if "locality" in record.get("types") :
            city = record.get('long_name')
            return city
    
    def get_state_code(self, record):
        #1616458060
        if "administrative_area_level_1" in record.get("types") :
            state = record.get('short_name')
            return state
        
    def get_country_code(self, record):
        #1616458061
        if "country" in record.get("types") :
            country = record.get('short_name')
            return country

    def get_state_location(self, record):
        #1616458062
        if "country" in record.get("types") :
            country = record.get('short_name')
            return country
        
    def odoo_get_state_id(self, country_code, state_code ):
        #1616458063
        country = self.env['res.country'].search([ ('code','=', country_code) ])
        state = self.env['res.country.state'].search([ 
            '&',
            ('country_id','=', country.id),
            ('code','=', state_code),
        ])
        if state:
            return state
        
    def get_current_google_key(self):
        #1616458064
        current_company = self.env.company
        google_key = self.env['website'].search([
            ('company_id','=',current_company.id)
        ])
            
        if len(google_key) > 1:
            google_key = google_key[0]['google_maps_api_key']
        else:
            google_key = google_key['google_maps_api_key']
        return google_key
    
    def same_country_code(self, g_country_code):
        #1616458065
        if self.country_id.code == g_country_code:
            return True
        else:
            return False
        
    @api.onchange('city_geolocation')
    def _onchange_state(self):
        #1616458066
        
        if self.city_geolocation:
            
            city_geolocation = self.city_geolocation

            base_url = "https://maps.googleapis.com/maps/api/timezone/json?"
            base_url = "{}location={}&timestamp={}&key={}".format(
                base_url,
                city_geolocation,
                int( time.time() ),
                self.get_current_google_key(),
            )

            r= requests.get(base_url)

            if r.status_code == 200:
                r_json = r.json()
                
                if r_json.get("status") == "ZERO_RESULTS":
                    self.write({
                        'timezone_name':'Time Zone not Found',
                    })
                    return

                if r_json.get("status") == "OK":
                    
                    timezone_id = r_json.get('timeZoneId')
                    timezone_name = r_json.get('timeZoneName')
                    dstOffset = r_json.get('dstOffset')
                    rawOffset = r_json.get('rawOffset')
                    self.write({
                        'tz' : timezone_id,
                        'timezone_name' : timezone_name
                    })
