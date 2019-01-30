# -*- coding: utf-8 -*-
{
    'name': 'Signup with Address, Phone and Date of Birth',
    'summary': 'Signup page with Address, Phone and Date of Birth Fields.',
    'description': '''Signup page with Address 
            - New Customer can give complete address with phone number while signup.
            - List of all States and Countries will be shown selected field in Signup page.
            - Add Date of Birth field.
            - You can choose whether Phone/Address/Date of Birth need to shown in Signup page in Configuration. 
            Default will be enabled.
            - Upload profile picture while sign up(Upcoming feature)
    ''',
    'author': 'Tintumon .M',
    'website': 'http://www.tintumon.co.in',
    'license': 'AGPL-3',
    'category': 'Website',
    'version': '0.1',
    'images': ['static/description/banner.jpg'],
    'depends': [
        'base',
        'auth_signup',
    ],
    'data': [
        'views/auth_signup_views.xml',
        'views/res_config_settings_views.xml',
        'views/res_partner_views.xml',
        'views/res_users_views.xml',
    ],
}
