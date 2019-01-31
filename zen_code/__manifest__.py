# -*- coding: utf-8 -*-
{
    'name': "Zen Code",
    'summary': """
        """,
    'description': """
    """,
    'author': "Supreeth",
    'website': "http://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',
    # any module necessary for this one to work correctly
    'depends': ['base','contacts','mail','portal'],
    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}