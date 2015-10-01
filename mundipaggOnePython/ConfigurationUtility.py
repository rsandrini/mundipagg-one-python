import json
import os


class ConfigurationUtility(object):
    def __init__(self, configuration='config.json'):
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), configuration), 'r') as config:
            self.__configuration = json.load(config)

    def merchant_key(self):
        return self.__configuration.get('merchant_key')

    def production_host_uri(self):
        return self.__configuration.get('production_host_uri')

    def sandbox_host_uri(self):
        return self.__configuration.get('sandbox_host_uri')

    def database(self):
        return self.__configuration.get('database')

    def mundipagg_key(self):
        return self.__configuration.get('mundipagg_key')
