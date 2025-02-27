# -*- coding: utf-8 -*-
{
    'name': "La Peliculera",

    'summary': "Gestión integral de alquiler de películas para videoclubes",

    'description': """
Módulo para Odoo que permite la gestión eficiente de un videoclub, incluyendo el alquiler de películas, control de stock, y administración de clientes.
    """,

    'author': "Abel Moro",
    'website': "https://github.com/AbelMoroEducaMadrid/LaPeliculeraOdooModule/tree/development",

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
        'security/security.xml',
        'views/views.xml',
        'views/templates.xml',
        'reports/informe_pelicula.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}