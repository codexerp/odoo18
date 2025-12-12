{
    'name': 'Codex Simple Login',
    'version': '0.1',
    'category': 'Tools',
    'summary': 'Simple login screen with Codex logo',
    'depends': ['web'],
    'data': [
        'views/codex_login_templates.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'codex_simple_login/static/src/css/codex_login.css',
        ],
    },
    'installable': True,
    'application': False,
}
