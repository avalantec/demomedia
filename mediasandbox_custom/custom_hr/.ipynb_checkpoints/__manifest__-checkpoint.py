# -*- coding: utf-8 -*-
{
    'name': "Custom Recruitment for Mediasandbox1",

    'summary': """
        Custom Recruitment for Mediasandbox""",

    'description': """
        Custom Recruitment for Mediasandbox
    """,

    'author': "Avalantec",
    'website': "http://www.avalantec.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','website', 'website_hr_recruitment' ,'hr_recruitment'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/website_hr_recruitment.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
