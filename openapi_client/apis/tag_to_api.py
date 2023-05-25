import typing_extensions

from openapi_client.apis.tags import TagValues
from openapi_client.apis.tags.teams_api import TeamsApi
from openapi_client.apis.tags.organizations_api import OrganizationsApi
from openapi_client.apis.tags.projects_api import ProjectsApi
from openapi_client.apis.tags.events_api import EventsApi
from openapi_client.apis.tags.releases_api import ReleasesApi
from openapi_client.apis.tags.integration_api import IntegrationApi
from openapi_client.apis.tags.scim_api import SCIMApi
from openapi_client.apis.tags.discover_api import DiscoverApi
from openapi_client.apis.tags.crons_api import CronsApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.TEAMS: TeamsApi,
        TagValues.ORGANIZATIONS: OrganizationsApi,
        TagValues.PROJECTS: ProjectsApi,
        TagValues.EVENTS: EventsApi,
        TagValues.RELEASES: ReleasesApi,
        TagValues.INTEGRATION: IntegrationApi,
        TagValues.SCIM: SCIMApi,
        TagValues.DISCOVER: DiscoverApi,
        TagValues.CRONS: CronsApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.TEAMS: TeamsApi,
        TagValues.ORGANIZATIONS: OrganizationsApi,
        TagValues.PROJECTS: ProjectsApi,
        TagValues.EVENTS: EventsApi,
        TagValues.RELEASES: ReleasesApi,
        TagValues.INTEGRATION: IntegrationApi,
        TagValues.SCIM: SCIMApi,
        TagValues.DISCOVER: DiscoverApi,
        TagValues.CRONS: CronsApi,
    }
)
