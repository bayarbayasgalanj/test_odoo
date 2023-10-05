# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Test module',
    'version': '1.0.1',
    'category': 'Purchase',
    'sequence': 20,
    'author': 'Bayarbayasgalan MGL',
    'summary': 'Purchase',
    'description': """
    """,
    'depends': ['base'],
    'data': [
        "security/security.xml",
        "security/ir.model.access.csv",
        "views/test_odoo_view.xml",
    ],
    'qweb': [],
    'website': 'https://www.linkedin.com/in/bayarbayasgalan-jagdal/',
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}