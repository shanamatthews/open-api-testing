# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from openapi_client.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    TEAMS = "Teams"
    ORGANIZATIONS = "Organizations"
    PROJECTS = "Projects"
    EVENTS = "Events"
    RELEASES = "Releases"
    INTEGRATION = "Integration"
    SCIM = "SCIM"
    DISCOVER = "Discover"
    CRONS = "Crons"
