from django.conf import settings

import requests
import urllib


class BadRequestError(Exception):
    pass


class NotFoundError(Exception):
    pass


class InvalidFilterError(Exception):
    pass


class Api(object):

    # WAR_FRENQUENCY_CHOICES = (
    #     ('always', 'Always'),
    #     ('moreThanOncePerWeek', 'More than once per week'),
    #     ('oncePerWeek', 'Once per week'),
    #     ('lessThanOncePerWeek', 'Less than once per week'),
    #     ('never', 'Never'),
    #     ('unknown', 'Unknown')
    # )

    CLANS_FILTERS = (
        'name',
        'war_frequency',
        'location_id',
        'min_members',
        'max_members',
        'min_clan_points',
        'min_clan_level',
        'limit',
        'after',
        'before'
    )

    def __init__(self, *args, **kwargs):
        self._headers = {
            "Accept": "application/json",
            "Authorization": "Bearer %s" % settings.COC_API_TOKEN
        }

    def process_response(self, response):
        if response.status_code == 200:
            return response.json()
        if response.status_code == 400:
            raise BadRequestError('[%s] %s' % (response.status_code, response.json().get('message')))
        if response.status_code == 400:
            raise NotFoundError('[%s] %s' % (response.status_code, response.json().get('message')))

    def clans(self, **kwargs):
        if not all([key in self.CLANS_FILTERS for key in kwargs.keys()]):
            raise InvalidFilterError("Invalid filter [%s]. Valid filters are %s" % (key, self.CLANS_FILTERS))

        filters = {}
        for key, value in kwargs:
            filter_snake_case = key.split('_')
            filter_camel_case = filter_snake_case[0] + "".join([word.title() for word in filter_snake_case[1:]])
            filters[filter_camel_case] = value

        response = requests.get("%s/clans" % settings.COC_API_BASE_URL, headers=self._headers, params=filters)

        json_response = self.process_response(response)
        return json_response.get('items')

    def clan(self, tag):
        url = "%s/clans/%s" % (settings.COC_API_BASE_URL, urllib.quote_plus(tag))
        response = requests.get(url, headers=self._headers)
        json_response = self.process_response(response)
        return json_response
