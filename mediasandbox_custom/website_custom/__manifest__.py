# -*- coding: utf-8 -*-
{
    'name': "Custom Website Code for Mediasandbox",

    'summary': """
        Module to custom the website""",

    'description': """
        Module to customize the website \n
        To hide the Header or Footer \n
        Open the Website \n
        Click on Edit \n
        Go To Options / Theme Options
    """,

    'author': "Avalantec",
    'website': "http://www.avalantec.com",
    'category': 'website',
    'version': '0.1',
    'depends': ['base','website'],

    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/website_layout.xml',
        'views/website_options.xml',
        
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
