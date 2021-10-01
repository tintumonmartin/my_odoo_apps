# -*- coding: utf-8 -*-
{
    'name': "Restrict Module Uninstall",
    'summary': """
        Used to Restrict Module Uninstall using password.""",
    'description': """
        Used to Restrict Module Uninstall using password.
        Prevent Apps from Being Uninstalled by Someone.
    """,
    'author': "Tintumon",
    'website': "https://tintumon.co.in",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'wizard/base_module_uninstall_views.xml',
    ],
    'images': ['static/description/uninstall_wizard.png'],
}
