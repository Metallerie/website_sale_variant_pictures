# -*- coding: utf-8 -*-
{
    'name': "website_sale_variant_pictures",

    'summary': """
        Ajoute un image au variant""",

    'description': """

    """,

    'author': "My Franck  Company",
    'website': "http://www.franckcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '12.0.1.0.2',
    # any module necessary for this one to work correctly
    'depends': ['base','website','website_sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/assets.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
