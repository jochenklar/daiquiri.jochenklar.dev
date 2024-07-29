from daiquiri.query.adapter import QueryFormAdapter


class ConeSearchQueryFormAdapter(QueryFormAdapter):

    def get_fields(self):
        return [
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
        ]

    def get_query_language(self, data):
        return 'adql-2.0'

    def get_query(self, data):
        return '''
SELECT ra, dec
FROM daiquiri_data_obs.stars
WHERE SQRT(POWER(ra - {ra}, 2) + POWER(dec - {dec}, 2)) <= {radius};
        '''.format(**data).strip()


class HaloMassQueryFormAdapter(QueryFormAdapter):

    def get_fields(self):
        return [
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
        ]

    def get_query_language(self, data):
        return 'adql-2.0'

    def get_query(self, data):
        return '''
SELECT *
FROM daiquiri_data_sim.halos
WHERE mass >= {min_mass} AND mass <= {max_mass}
ORDER BY mass DESC;
        '''.format(**data).strip()
