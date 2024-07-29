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
        'template': 'query/new/query_form_cone.html',
        'fields': [
            {
                'key': 'ra',
                'type': 'number',
                'label': 'RA',
                'help': 'Right ascension in degrees (decimal form)',
                'default_value': 10.684708,
                'width': 4
            },
            {
                'key': 'dec',
                'type': 'number',
                'label': 'DEC',
                'help': 'Declination in degrees (decimal form)',
                'default_value': 41.26875,
                'width': 4
            },
            {
                'key': 'radius',
                'type': 'number',
                'label': 'Radius',
                'help': 'Radius in degrees',
                'default_value': 10,
                'width': 4
            }
        ],
        'submit': 'Submit new cone search',
        'adapter': 'jochenklar.adapter.ConeSearchQueryFormAdapter'
    },
    {
        'key': 'mass',
        'label': 'Halo mass range',
        'template': 'query/new/query_form_halo_mass.html',
        'fields': [
            {
                'key': 'min_mass',
                'type': 'number',
                'label': 'Minimum halo mass',
                'help': 'Minimum halo mass (in solar masses)',
                'default_value': 1e+15,
                'width': 6
            },
            {
                'key': 'max_mass',
                'type': 'number',
                'label': 'Maximum halo mass',
                'help': 'Maximum halo mass (in solar masses)',
                'default_value': 3e+15,
                'width': 6
            }
        ],
        'submit': 'Submit new cone search',
        'adapter': 'jochenklar.adapter.HaloMassQueryFormAdapter'
    },
    {
        'key': 'upload',
        'label': 'Upload VOTable',
        'template': 'query/new/query_form_upload.html'
    }
]
