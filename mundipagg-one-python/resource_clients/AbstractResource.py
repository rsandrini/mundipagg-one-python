from abc import ABCMeta
from PlatformEnvironment import PlatformEnvironment
import json
import uuid


class AbstractResource(object):

    __metaclass__ = ABCMeta

    def __init__(self, merchant_key=None, environment=None, http_content_type=None, resource_name=None, host_uri=None):
        if merchant_key is None:
            merchant_key = self.get_configuration_key('GatewayService.MerchantKey')

        self.merchant_key = merchant_key
        self.plataform_environment = environment
        self.http_content_type = http_content_type

        if host_uri is not None:
            self.host_uri = host_uri
        else:
            self.host_uri = self.get_service_uri(environment)

        self.resource_name = resource_name

    def get_service_uri(self, environment):
        switch_uri = {PlatformEnvironment.production: self.get_configuration_string("GatewayService.ProductionHostUri"),
                      PlatformEnvironment.sand_box: self.get_configuration_string("GatewayService.SandboxHostUri")}

        return switch_uri.get(environment)

    @staticmethod
    def get_configuration_string(configuration_name):
        with open('config.json') as config_file:
            config = json.load(config_file)

        configuration = config.get(configuration_name)
        if configuration:
            return configuration
        else:
            raise ValueError('Missing configuration: ' + configuration_name)

    @staticmethod
    def get_configuration_key(configuration_name):
        with open('config.json') as config_file:
            config = json.load(config_file)

        configuration = config.get(configuration_name)
        if configuration:
            return uuid.UUID(configuration)
        else:
            raise ValueError('Missing configuration: ' + configuration_name)