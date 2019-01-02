# -*- coding: utf-8 -*-
{
    'name': "Employee Car Requestt",

    'summary': """
        This is shot description 
        and this can have multiple line""",

    'description': """
        The module purpose is for learning creating a odoo module
    """,

    'author': "SkyERP Co., Ltd.",
    'website': "http://skyerp.net",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],cd
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}