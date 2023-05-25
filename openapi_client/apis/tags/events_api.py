# coding: utf-8

"""
    API Reference

    Sentry Public API  # noqa: E501

    The version of the OpenAPI document: v0
    Contact: partners@sentry.io
    Generated by: https://openapi-generator.tech
"""

from openapi_client.paths.api_0_projects_organization_slug_project_slug_issues_.put import BulkMutateAListOfIssues
from openapi_client.paths.api_0_projects_organization_slug_project_slug_issues_.delete import BulkRemoveAListOfIssues
from openapi_client.paths.api_0_projects_organization_slug_project_slug_events_event_id_source_map_debug_.get import DebugIssuesRelatedToSourceMapsForAGivenEvent
from openapi_client.paths.api_0_projects_organization_slug_project_slug_events_.get import ListAProjectsEvents
from openapi_client.paths.api_0_projects_organization_slug_project_slug_issues_.get import ListAProjectsIssues
from openapi_client.paths.api_0_issues_issue_id_tags_key_values_.get import ListATagsValuesRelatedToAnIssue
from openapi_client.paths.api_0_issues_issue_id_events_.get import ListAnIssuesEvents
from openapi_client.paths.api_0_issues_issue_id_hashes_.get import ListAnIssuesHashes
from openapi_client.paths.api_0_issues_issue_id_.delete import RemoveAnIssue
from openapi_client.paths.api_0_projects_organization_slug_project_slug_events_event_id_.get import RetrieveAnEventForAProject
from openapi_client.paths.api_0_issues_issue_id_.get import RetrieveAnIssue
from openapi_client.paths.api_0_issues_issue_id_tags_key_.get import RetrieveTagDetails
from openapi_client.paths.api_0_issues_issue_id_events_latest_.get import RetrieveTheLatestEventForAnIssue
from openapi_client.paths.api_0_issues_issue_id_events_oldest_.get import RetrieveTheOldestEventForAnIssue
from openapi_client.paths.api_0_issues_issue_id_.put import UpdateAnIssue


class EventsApi(
    BulkMutateAListOfIssues,
    BulkRemoveAListOfIssues,
    DebugIssuesRelatedToSourceMapsForAGivenEvent,
    ListAProjectsEvents,
    ListAProjectsIssues,
    ListATagsValuesRelatedToAnIssue,
    ListAnIssuesEvents,
    ListAnIssuesHashes,
    RemoveAnIssue,
    RetrieveAnEventForAProject,
    RetrieveAnIssue,
    RetrieveTagDetails,
    RetrieveTheLatestEventForAnIssue,
    RetrieveTheOldestEventForAnIssue,
    UpdateAnIssue,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
