# -*- coding: utf-8 -*-
{
    'name': "Prestamos pádel",

    'summary': """
        Modulo para prestamos de material de pádel""",

    'description': """
        Modulo no que poderás xestionar material para prestar.
    """,

    'author': "a21sergiobp",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/loans_material.xml',
        'security/ir.model.access.csv',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
