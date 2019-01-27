# -*- coding: utf-8 -*-
{
    'name': "Signup with Address",
    'summary': """Signup page with Address.""",
    'description': """Signup page with Address 
            - New Customer can give complete address with phone number while signup.
            - List of States and Countries will be selected.
    """,
    'author': "Tintumon .M",
    'website': "http://www.tintumon.co.in",
    'license': "AGPL-3",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': [
        'base',
        'auth_signup',
    ],
    'data': [
        'views/auth_signup_views.xml',
    ],
}
