{
    'name': 'CDX Rebranding',
    'summary': 'Replace Odoo branding with cdx',
    'version': '1.0',
    'category': 'Tools',
    'depends': ['web', 'mail'],
    'data': [
        'views/webclient_templates.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'cdx_rebranding/static/src/img/*',
        ],
        'web.assets_frontend': [
            'cdx_rebranding/static/src/img/*',
        ],
    },
    'installable': True,
}
