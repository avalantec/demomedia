# -*- coding: utf-8 -*-
{
    'name': "google_timezone",

    'summary': """
        Module that gets the state and timezone from the zip code,
        using the google services
        """,

    'description': """
        Module that gets the state and timezone from the zip code,
        using the google services
    """,

    'author': "Avalantec",
    'website': "http://www.avalantec.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'base_geolocalize'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        #'views/views.xml',
        #'views/templates.xml',
        'views/res_partner.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
