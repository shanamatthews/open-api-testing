# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import openapi_client
from openapi_client.paths.api_0_projects_organization_slug_project_slug_hooks_hook_id_ import delete  # noqa: E501
from openapi_client import configuration, schemas, api_client

from .. import ApiTestMixin


class TestApi0ProjectsOrganizationSlugProjectSlugHooksHookId(ApiTestMixin, unittest.TestCase):
    """
    Api0ProjectsOrganizationSlugProjectSlugHooksHookId unit test stubs
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = delete.ApiFordelete(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 204
    response_body = ''


if __name__ == '__main__':
    unittest.main()
