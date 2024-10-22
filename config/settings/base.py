from . import ADDITIONAL_APPS, DJANGO_APPS

SITE_IDENTIFIER = 'daiquiri.jochenklar.dev'
SITE_TITLE = 'daiquiri.jochenklar.dev'
SITE_DESCRIPTION = 'A demo application for the daiquiri framework.'
SITE_LICENSE = 'CC0'
SITE_CREATOR = 'Jochen Klar'
SITE_CONTACT = {
    'name': 'Jochen Klar',
    'email': 'admin@jochenklar.de',
}
SITE_PUBLISHER = 'Jochen Klar'
SITE_CREATED = '2024-07-01'
SITE_UPDATED = '2024-07-01'

INSTALLED_APPS = DJANGO_APPS + [
    'jochenklar',
    'daiquiri.auth',
    'daiquiri.conesearch',
    'daiquiri.contact',
    'daiquiri.core',
    'daiquiri.datalink',
    'daiquiri.files',
    'daiquiri.jobs',
    'daiquiri.metadata',
    'daiquiri.oai',
    'daiquiri.query',
    'daiquiri.registry',
    'daiquiri.serve',
    'daiquiri.stats',
    'daiquiri.tap',
    'daiquiri.uws',
] + ADDITIONAL_APPS

QUERY_ANONYMOUS = True
QUERY_LANGUAGES = [
    {
        'key': 'adql',
        'version': 2.0,
        'label': 'ADQL',
        'description': '',
        'quote_char': '"'
    },
    {
        'key': 'postgresql',
        'version': 9.6,
        'label': 'PostgreSQL',
        'description': '',
        'quote_char': '"'
    }
]

QUERY_QUEUES = [
    {
        'key': 'short',
        'label': 'Short',
        'timeout': 10,
        'concurency': 2,
        'access_level': 'PUBLIC',
        'groups': []
    },
    {
        'key': 'long',
        'label': 'Long',
        'timeout': 120,
        'access_level': 'PUBLIC',
        'groups': []
    }
]

QUERY_FORMS = [
    {
        'key': 'sql',
        'label': 'SQL query',
        'template': 'query/new/query_form_sql.html'
    },
    {
        'key': 'cone',
        'label': 'Source cone search',
        'submit': 'Submit new cone search',
        'template': 'query/new/query_form_cone.html',
        'adapter': 'jochenklar.adapter.ConeSearchQueryFormAdapter'
    },
    {
        'key': 'mass',
        'label': 'Halo mass range',
        'submit': 'Submit new halo mass range search',
        'template': 'query/new/query_form_halo_mass.html',
        'adapter': 'jochenklar.adapter.HaloMassQueryFormAdapter'
    },
    {
        'key': 'upload',
        'label': 'Upload VOTable',
        'template': 'query/new/query_form_upload.html'
    }
]
