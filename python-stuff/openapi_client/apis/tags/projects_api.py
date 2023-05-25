# coding: utf-8

"""
    API Reference

    Sentry Public API  # noqa: E501

    The version of the OpenAPI document: v0
    Contact: partners@sentry.io
    Generated by: https://openapi-generator.tech
"""

from openapi_client.paths.api_0_projects_organization_slug_project_slug_keys_.post import CreateANewClientKey
from openapi_client.paths.api_0_projects_organization_slug_project_slug_keys_key_id_.delete import DeleteAClientKey
from openapi_client.paths.api_0_projects_organization_slug_project_slug_.delete import DeleteAProject
from openapi_client.paths.api_0_projects_organization_slug_project_slug_files_dsyms_.delete import DeleteASpecificProjectsDebugInformationFile
from openapi_client.paths.api_0_projects_organization_slug_project_slug_keys_.get import ListAProjectsClientKeys
from openapi_client.paths.api_0_projects_organization_slug_project_slug_files_dsyms_.get import ListAProjectsDebugInformationFiles
from openapi_client.paths.api_0_projects_organization_slug_project_slug_hooks_.get import ListAProjectsServiceHooks
from openapi_client.paths.api_0_projects_organization_slug_project_slug_user_feedback_.get import ListAProjectsUserFeedback
from openapi_client.paths.api_0_projects_organization_slug_project_slug_users_.get import ListAProjectsUsers
from openapi_client.paths.api_0_projects_organization_slug_project_slug_tags_key_values_.get import ListATagsValues
from openapi_client.paths.api_0_projects_.get import ListYourProjects
from openapi_client.paths.api_0_projects_organization_slug_project_slug_hooks_.post import RegisterANewServiceHook
from openapi_client.paths.api_0_projects_organization_slug_project_slug_hooks_hook_id_.delete import RemoveAServiceHook
from openapi_client.paths.api_0_projects_organization_slug_project_slug_.get import RetrieveAProject
from openapi_client.paths.api_0_projects_organization_slug_project_slug_hooks_hook_id_.get import RetrieveAServiceHook
from openapi_client.paths.api_0_projects_organization_slug_project_slug_stats_.get import RetrieveEventCountsForAProject
from openapi_client.paths.api_0_projects_organization_slug_project_slug_user_feedback_.post import SubmitUserFeedback
from openapi_client.paths.api_0_projects_organization_slug_project_slug_keys_key_id_.put import UpdateAClientKey
from openapi_client.paths.api_0_projects_organization_slug_project_slug_.put import UpdateAProject
from openapi_client.paths.api_0_projects_organization_slug_project_slug_hooks_hook_id_.put import UpdateAServiceHook
from openapi_client.paths.api_0_projects_organization_slug_project_slug_files_dsyms_.post import UploadANewFile


class ProjectsApi(
    CreateANewClientKey,
    DeleteAClientKey,
    DeleteAProject,
    DeleteASpecificProjectsDebugInformationFile,
    ListAProjectsClientKeys,
    ListAProjectsDebugInformationFiles,
    ListAProjectsServiceHooks,
    ListAProjectsUserFeedback,
    ListAProjectsUsers,
    ListATagsValues,
    ListYourProjects,
    RegisterANewServiceHook,
    RemoveAServiceHook,
    RetrieveAProject,
    RetrieveAServiceHook,
    RetrieveEventCountsForAProject,
    SubmitUserFeedback,
    UpdateAClientKey,
    UpdateAProject,
    UpdateAServiceHook,
    UploadANewFile,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass