# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import openapi_client
from openapi_client.paths.api_0_organizations_organization_slug_sentry_app_installations_ import get  # noqa: E501
from openapi_client import configuration, schemas, api_client

from .. import ApiTestMixin


class TestApi0OrganizationsOrganizationSlugSentryAppInstallations(ApiTestMixin, unittest.TestCase):
    """
    Api0OrganizationsOrganizationSlugSentryAppInstallations unit test stubs
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = get.ApiForget(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
