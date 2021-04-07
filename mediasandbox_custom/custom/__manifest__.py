# -*- coding: utf-8 -*-
{
    'name': "Custom CRM Code for Mediasandbox",

    'summary': """
        Custom Code for the CRM""",

    'description': """
        Custom Code for the CRM
    """,

    'author': "Avalantec",
    'website': "http://www.avalantec.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.2',

    # any module necessary for this one to work correctly
    'depends': ['base','crm'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/crm_lead_form.xml',
        'views/res_partner.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
