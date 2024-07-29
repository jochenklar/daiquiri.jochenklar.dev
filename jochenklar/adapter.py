from daiquiri.query.adapter import QueryFormAdapter


class ConeSearchQueryFormAdapter(QueryFormAdapter):

    def get_query_language(self, data):
        return 'adql-2.0'

    def get_query(self, data):
        return '''
SELECT ra, dec
FROM daiquiri_data_obs.stars
WHERE SQRT(POWER(ra - {ra}, 2) + POWER(dec - {dec}, 2)) <= {radius};
        '''.format(**data).strip()


class HaloMassQueryFormAdapter(QueryFormAdapter):

    def get_query_language(self, data):
        return 'adql-2.0'

    def get_query(self, data):
        return '''
SELECT *
FROM daiquiri_data_sim.halos
WHERE mass >= {min_mass} AND mass <= {max_mass}
ORDER BY mass DESC;
        '''.format(**data).strip()
