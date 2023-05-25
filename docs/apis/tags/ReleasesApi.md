<a id="__pageTop"></a>
# openapi_client.apis.tags.releases_api.ReleasesApi

All URIs are relative to *https://sentry.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_a_new_deploy_for_an_organization**](#create_a_new_deploy_for_an_organization) | **post** /api/0/organizations/{organization_slug}/releases/{version}/deploys/ | 
[**create_a_new_release_for_an_organization**](#create_a_new_release_for_an_organization) | **post** /api/0/organizations/{organization_slug}/releases/ | 
[**delete_a_project_releases_file**](#delete_a_project_releases_file) | **delete** /api/0/projects/{organization_slug}/{project_slug}/releases/{version}/files/{file_id}/ | 
[**delete_an_organization_releases_file**](#delete_an_organization_releases_file) | **delete** /api/0/organizations/{organization_slug}/releases/{version}/files/{file_id}/ | 
[**delete_an_organizations_release**](#delete_an_organizations_release) | **delete** /api/0/organizations/{organization_slug}/releases/{version}/ | 
[**list_a_project_releases_commits**](#list_a_project_releases_commits) | **get** /api/0/projects/{organization_slug}/{project_slug}/releases/{version}/commits/ | 
[**list_a_projects_release_files**](#list_a_projects_release_files) | **get** /api/0/projects/{organization_slug}/{project_slug}/releases/{version}/files/ | 
[**list_a_releases_deploys**](#list_a_releases_deploys) | **get** /api/0/organizations/{organization_slug}/releases/{version}/deploys/ | 
[**list_an_organization_releases_commits**](#list_an_organization_releases_commits) | **get** /api/0/organizations/{organization_slug}/releases/{version}/commits/ | 
[**list_an_organizations_release_files**](#list_an_organizations_release_files) | **get** /api/0/organizations/{organization_slug}/releases/{version}/files/ | 
[**list_an_organizations_releases**](#list_an_organizations_releases) | **get** /api/0/organizations/{organization_slug}/releases/ | 
[**list_issues_to_be_resolved_in_a_particular_release**](#list_issues_to_be_resolved_in_a_particular_release) | **get** /api/0/projects/{organization_slug}/{project_slug}/releases/{version}/resolved/ | 
[**retrieve_a_project_releases_file**](#retrieve_a_project_releases_file) | **get** /api/0/projects/{organization_slug}/{project_slug}/releases/{version}/files/{file_id}/ | 
[**retrieve_an_organization_releases_file**](#retrieve_an_organization_releases_file) | **get** /api/0/organizations/{organization_slug}/releases/{version}/files/{file_id}/ | 
[**retrieve_an_organizations_releases**](#retrieve_an_organizations_releases) | **get** /api/0/organizations/{organization_slug}/releases/{version}/ | 
[**retrieve_files_changed_in_a_releases_commits**](#retrieve_files_changed_in_a_releases_commits) | **get** /api/0/organizations/{organization_slug}/releases/{version}/commitfiles/ | 
[**retrieve_release_health_session_statistics**](#retrieve_release_health_session_statistics) | **get** /api/0/organizations/{organization_slug}/sessions/ | 
[**update_a_project_release_file**](#update_a_project_release_file) | **put** /api/0/projects/{organization_slug}/{project_slug}/releases/{version}/files/{file_id}/ | 
[**update_an_organization_release_file**](#update_an_organization_release_file) | **put** /api/0/organizations/{organization_slug}/releases/{version}/files/{file_id}/ | 
[**update_an_organizations_release**](#update_an_organizations_release) | **put** /api/0/organizations/{organization_slug}/releases/{version}/ | 
[**upload_a_new_organization_release_file**](#upload_a_new_organization_release_file) | **post** /api/0/organizations/{organization_slug}/releases/{version}/files/ | 
[**upload_a_new_project_release_file**](#upload_a_new_project_release_file) | **post** /api/0/projects/{organization_slug}/{project_slug}/releases/{version}/files/ | 

# **create_a_new_deploy_for_an_organization**
<a id="create_a_new_deploy_for_an_organization"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_a_new_deploy_for_an_organization(organization_slugversion)



Create a deploy.

### Example

* Bearer Authentication (auth_token):
```python
import openapi_client
from openapi_client.apis.tags import releases_api
from pprint import pprint
# Defining the host is optional and defaults to https://sentry.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://sentry.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: auth_token
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = releases_api.ReleasesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'organization_slug': "organization_slug_example",
        'version': "version_example",
    }
    try:
        api_response = api_instance.create_a_new_deploy_for_an_organization(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ReleasesApi->create_a_new_deploy_for_an_organization: %s\n" % e)

    # example passing only optional values
    path_params = {
        'organization_slug': "organization_slug_example",
        'version': "version_example",
    }
    body = dict(
        environment="environment_example",
        url="url_example",
        name="name_example",
null,
        date_started="1970-01-01T00:00:00.00Z",
        date_finished="1970-01-01T00:00:00.00Z",
    )
    try:
        api_response = api_instance.create_a_new_deploy_for_an_organization(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ReleasesApi->create_a_new_deploy_for_an_organization: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**environment** | str,  | str,  | The environment you&#x27;re deploying to. | 
**url** | str,  | str,  | The optional URL that points to the deploy. | [optional] 
**name** | str,  | str,  | The optional name of the deploy. | [optional] 
**projects** |  |  | The optional list of projects to deploy. | [optional] 
**dateStarted** | str, datetime,  | str,  | An optional date that indicates when the deploy started. | [optional] value must conform to RFC-3339 date-time
**dateFinished** | str, datetime,  | str,  | An optional date that indicates when the deploy ended. If not provided, the current time is used. | [optional] value must conform to RFC-3339 date-time
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
organization_slug | OrganizationSlugSchema | | 
version | VersionSchema | | 

# OrganizationSlugSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#create_a_new_deploy_for_an_organization.ApiResponseFor201) | Success
208 | [ApiResponseFor208](#create_a_new_deploy_for_an_organization.ApiResponseFor208) | Already Reported
403 | [ApiResponseFor403](#create_a_new_deploy_for_an_organization.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#create_a_new_deploy_for_an_organization.ApiResponseFor404) | Not Found

#### create_a_new_deploy_for_an_organization.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**environment** | str,  | str,  |  | 
**dateStarted** | None, str, datetime,  | NoneClass, str,  |  | value must conform to RFC-3339 date-time
**dateFinished** | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time
**name** | None, str,  | NoneClass, str,  |  | 
**id** | str,  | str,  |  | 
**url** | None, str,  | NoneClass, str,  |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### create_a_new_deploy_for_an_organization.ApiResponseFor208
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### create_a_new_deploy_for_an_organization.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### create_a_new_deploy_for_an_organization.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[auth_token](../../../README.md#auth_token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_a_new_release_for_an_organization**
<a id="create_a_new_release_for_an_organization"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_a_new_release_for_an_organization(organization_slug)



Create a new release for the given organization.  Releases are used by Sentry to improve its error reporting abilities by correlating first seen events with the release that might have introduced the problem. Releases are also necessary for source maps and other debug features that require manual upload for functioning well.

### Example

* Bearer Authentication (auth_token):
```python
import openapi_client
from openapi_client.apis.tags import releases_api
from pprint import pprint
# Defining the host is optional and defaults to https://sentry.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://sentry.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: auth_token
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = releases_api.ReleasesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'organization_slug': "organization_slug_example",
    }
    try:
        api_response = api_instance.create_a_new_release_for_an_organization(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ReleasesApi->create_a_new_release_for_an_organization: %s\n" % e)

    # example passing only optional values
    path_params = {
        'organization_slug': "organization_slug_example",
    }
    body = dict(
        version="version_example",
        ref="ref_example",
        url="url_example",
        projects=[
            "projects_example"
        ],
        date_released="1970-01-01T00:00:00.00Z",
        commits=[
            dict(
                patch_set=[
                    dict(
                        path="path_example",
                        type="A",
                    )
                ],
                repository="repository_example",
                author_name="author_name_example",
                author_email="author_email_example",
                timestamp="1970-01-01T00:00:00.00Z",
                message="message_example",
                id="id_example",
            )
        ],
        refs=[
            dict(
                repository="repository_example",
                commit="commit_example",
                previous_commit="previous_commit_example",
            )
        ],
    )
    try:
        api_response = api_instance.create_a_new_release_for_an_organization(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ReleasesApi->create_a_new_release_for_an_organization: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[projects](#projects)** | list, tuple,  | tuple,  | A list of project slugs that are involved in this release. | 
**version** | str,  | str,  | A version identifier for this release. Can be a version number, a commit hash, etc. | 
**ref** | str,  | str,  | An optional commit reference. This is useful if a tagged version has been provided. | [optional] 
**url** | str,  | str,  | A URL that points to the release. This can be the path to an online interface to the source code for instance | [optional] 
**dateReleased** | str, datetime,  | str,  | An optional date that indicates when the release went live. If not provided the current time is assumed. | [optional] value must conform to RFC-3339 date-time
**[commits](#commits)** | list, tuple,  | tuple,  | An optional list of commit data to be associated with the release. Commits must include parameters &#x60;id&#x60; (the SHA of the commit), and can optionally include &#x60;repository&#x60;, &#x60;message&#x60;, &#x60;patch_set&#x60;, &#x60;author_name&#x60;, &#x60;author_email&#x60;, and &#x60;timestamp&#x60;. | [optional] 
**[refs](#refs)** | list, tuple,  | tuple,  | An optional way to indicate the start and end commits for each repository included in a release. Head commits must include parameters &#x60;repository&#x60; and &#x60;commit&#x60; (the HEAD sha). They can optionally include &#x60;previousCommit&#x60; (the sha of the HEAD of the previous release), which should be specified if this is the first time you&#x27;ve sent commit data. &#x60;commit&#x60; may contain a range in the form of &#x60;previousCommit..commit&#x60;. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# projects

A list of project slugs that are involved in this release.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A list of project slugs that are involved in this release. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# commits

An optional list of commit data to be associated with the release. Commits must include parameters `id` (the SHA of the commit), and can optionally include `repository`, `message`, `patch_set`, `author_name`, `author_email`, and `timestamp`.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | An optional list of commit data to be associated with the release. Commits must include parameters &#x60;id&#x60; (the SHA of the commit), and can optionally include &#x60;repository&#x60;, &#x60;message&#x60;, &#x60;patch_set&#x60;, &#x60;author_name&#x60;, &#x60;author_email&#x60;, and &#x60;timestamp&#x60;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[patch_set](#patch_set)** | list, tuple,  | tuple,  | A list of the files that have been changed in the commit. Specifying the patch_set is necessary to power suspect commits and suggested assignees. | [optional] 
**repository** | str,  | str,  | The full name of the repository the commit belongs to. If this field is not given Sentry will generate a name in the form: u&#x27;organization-&lt;organization_id&gt;&#x27; (i.e. if the organization id is 123, then the generated repository name will be u&#x27;organization-123). | [optional] 
**author_name** | str,  | str,  | The name of the commit author. | [optional] 
**author_email** | str,  | str,  | The email of the commit author. The commit author&#x27;s email is required to enable the suggested assignee feature. | [optional] 
**timestamp** | str, datetime,  | str,  | The commit timestamp is used to sort the commits given. If a timestamp is not included, the commits will remain sorted in the order given. | [optional] value must conform to RFC-3339 date-time
**message** | str,  | str,  | The commit message. | [optional] 
**id** | str,  | str,  | The commit ID (the commit SHA). | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# patch_set

A list of the files that have been changed in the commit. Specifying the patch_set is necessary to power suspect commits and suggested assignees.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A list of the files that have been changed in the commit. Specifying the patch_set is necessary to power suspect commits and suggested assignees. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**path** | str,  | str,  | The path to the file. Both forward and backward slashes are supported. | 
**type** | str,  | str,  | The type of change that happened in the commit. | must be one of ["A", "M", "D", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# refs

An optional way to indicate the start and end commits for each repository included in a release. Head commits must include parameters `repository` and `commit` (the HEAD sha). They can optionally include `previousCommit` (the sha of the HEAD of the previous release), which should be specified if this is the first time you've sent commit data. `commit` may contain a range in the form of `previousCommit..commit`.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | An optional way to indicate the start and end commits for each repository included in a release. Head commits must include parameters &#x60;repository&#x60; and &#x60;commit&#x60; (the HEAD sha). They can optionally include &#x60;previousCommit&#x60; (the sha of the HEAD of the previous release), which should be specified if this is the first time you&#x27;ve sent commit data. &#x60;commit&#x60; may contain a range in the form of &#x60;previousCommit..commit&#x60;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**repository** | str,  | str,  | The full name of the repository the commit belongs to. | [optional] 
**commit** | str,  | str,  | The current release&#x27;s commit. | [optional] 
**previousCommit** | str,  | str,  | The previous release&#x27;s commit. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
organization_slug | OrganizationSlugSchema | | 

# OrganizationSlugSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#create_a_new_release_for_an_organization.ApiResponseFor201) | Success
400 | [ApiResponseFor400](#create_a_new_release_for_an_organization.ApiResponseFor400) | Bad Input
403 | [ApiResponseFor403](#create_a_new_release_for_an_organization.ApiResponseFor403) | Forbidden

#### create_a_new_release_for_an_organization.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[owner](#owner)** | dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  |  | 
**shortVersion** | str,  | str,  |  | 
**[projects](#projects)** | list, tuple,  | tuple,  |  | 
**[data](#data)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 
**commitCount** | decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer
**[lastCommit](#lastCommit)** | dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  |  | 
**[lastDeploy](#lastDeploy)** | dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  |  | 
**version** | str,  | str,  |  | 
**url** | None, str,  | NoneClass, str,  |  | 
**newGroups** | decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer
**ref** | None, str,  | NoneClass, str,  |  | 
**dateCreated** | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time
**firstEvent** | None, str, datetime,  | NoneClass, str,  |  | value must conform to RFC-3339 date-time
**lastEvent** | None, str, datetime,  | NoneClass, str,  |  | value must conform to RFC-3339 date-time
**deployCount** | decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer
**dateReleased** | None, str, datetime,  | NoneClass, str,  |  | value must conform to RFC-3339 date-time
**[authors](#authors)** | list, tuple,  | tuple,  |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# authors

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# data

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# lastCommit

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  |  | 

# lastDeploy

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### oneOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[one_of_0](#one_of_0) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 
[one_of_1](#one_of_1) | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

# one_of_0

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**environment** | str,  | str,  |  | 
**dateStarted** | None, str, datetime,  | NoneClass, str,  |  | value must conform to RFC-3339 date-time
**dateFinished** | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time
**name** | None, str,  | NoneClass, str,  |  | 
**id** | str,  | str,  |  | 
**url** | None, str,  | NoneClass, str,  |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# one_of_1

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### not
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[not_schema](#not_schema) | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

# not_schema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### anyOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[any_of_0](#any_of_0) | str,  | str,  |  | 
[any_of_1](#any_of_1) | decimal.Decimal, int, float,  | decimal.Decimal,  |  | 
[any_of_2](#any_of_2) | bool,  | BoolClass,  |  | 
[any_of_3](#any_of_3) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 
[any_of_4](#any_of_4) | list, tuple,  | tuple,  |  | 

# any_of_0

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# any_of_1

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  |  | 

# any_of_2

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# any_of_3

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# any_of_4

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

# owner

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  |  | 

# projects

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  |  | [optional] 
**slug** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### create_a_new_release_for_an_organization.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### create_a_new_release_for_an_organization.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[auth_token](../../../README.md#auth_token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_a_project_releases_file**
<a id="delete_a_project_releases_file"></a>
> delete_a_project_releases_file(organization_slugproject_slugversionfile_id)



Delete a file for a given release.

### Example

* Bearer Authentication (auth_token):
```python
import openapi_client
from openapi_client.apis.tags import releases_api
from pprint import pprint
# Defining the host is optional and defaults to https://sentry.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://sentry.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: auth_token
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = releases_api.ReleasesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'organization_slug': "organization_slug_example",
        'project_slug': "project_slug_example",
        'version': "version_example",
        'file_id': "file_id_example",
    }
    try:
        api_response = api_instance.delete_a_project_releases_file(
            path_params=path_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling ReleasesApi->delete_a_project_releases_file: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
organization_slug | OrganizationSlugSchema | | 
project_slug | ProjectSlugSchema | | 
version | VersionSchema | | 
file_id | FileIdSchema | | 

# OrganizationSlugSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ProjectSlugSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FileIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#delete_a_project_releases_file.ApiResponseFor204) | Success
403 | [ApiResponseFor403](#delete_a_project_releases_file.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#delete_a_project_releases_file.ApiResponseFor404) | Not Found

#### delete_a_project_releases_file.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_a_project_releases_file.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_a_project_releases_file.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[auth_token](../../../README.md#auth_token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_an_organization_releases_file**
<a id="delete_an_organization_releases_file"></a>
> delete_an_organization_releases_file(organization_slugversionfile_id)



Delete a file for a given release.

### Example

* Bearer Authentication (auth_token):
```python
import openapi_client
from openapi_client.apis.tags import releases_api
from pprint import pprint
# Defining the host is optional and defaults to https://sentry.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://sentry.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: auth_token
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = releases_api.ReleasesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'organization_slug': "organization_slug_example",
        'version': "version_example",
        'file_id': "file_id_example",
    }
    try:
        api_response = api_instance.delete_an_organization_releases_file(
            path_params=path_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling ReleasesApi->delete_an_organization_releases_file: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
organization_slug | OrganizationSlugSchema | | 
version | VersionSchema | | 
file_id | FileIdSchema | | 

# OrganizationSlugSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FileIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#delete_an_organization_releases_file.ApiResponseFor204) | Success
403 | [ApiResponseFor403](#delete_an_organization_releases_file.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#delete_an_organization_releases_file.ApiResponseFor404) | Not Found

#### delete_an_organization_releases_file.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_an_organization_releases_file.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_an_organization_releases_file.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[auth_token](../../../README.md#auth_token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_an_organizations_release**
<a id="delete_an_organizations_release"></a>
> delete_an_organizations_release(organization_slugversion)



Delete a release for a given organization.

### Example

* Bearer Authentication (auth_token):
```python
import openapi_client
from openapi_client.apis.tags import releases_api
from pprint import pprint
# Defining the host is optional and defaults to https://sentry.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://sentry.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: auth_token
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = releases_api.ReleasesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'organization_slug': "organization_slug_example",
        'version': "version_example",
    }
    try:
        api_response = api_instance.delete_an_organizations_release(
            path_params=path_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling ReleasesApi->delete_an_organizations_release: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
organization_slug | OrganizationSlugSchema | | 
version | VersionSchema | | 

# OrganizationSlugSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#delete_an_organizations_release.ApiResponseFor204) | Success

#### delete_an_organizations_release.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[auth_token](../../../README.md#auth_token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_a_project_releases_commits**
<a id="list_a_project_releases_commits"></a>
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] list_a_project_releases_commits(organization_slugproject_slugversion)



List a project release's commits.

### Example

* Bearer Authentication (auth_token):
```python
import openapi_client
from openapi_client.apis.tags import releases_api
from pprint import pprint
# Defining the host is optional and defaults to https://sentry.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://sentry.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: auth_token
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = releases_api.ReleasesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'organization_slug': "organization_slug_example",
        'project_slug': "project_slug_example",
        'version': "version_example",
    }
    try:
        api_response = api_instance.list_a_project_releases_commits(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ReleasesApi->list_a_project_releases_commits: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
organization_slug | OrganizationSlugSchema | | 
project_slug | ProjectSlugSchema | | 
version | VersionSchema | | 

# OrganizationSlugSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ProjectSlugSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_a_project_releases_commits.ApiResponseFor200) | Success
403 | [ApiResponseFor403](#list_a_project_releases_commits.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#list_a_project_releases_commits.ApiResponseFor404) | Not Found

#### list_a_project_releases_commits.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**dateCreated** | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time
**id** | str,  | str,  |  | 
**message** | None, str,  | NoneClass, str,  |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### list_a_project_releases_commits.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### list_a_project_releases_commits.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[auth_token](../../../README.md#auth_token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_a_projects_release_files**
<a id="list_a_projects_release_files"></a>
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] list_a_projects_release_files(organization_slugproject_slugversion)



Return a list of files for a given release.

### Example

* Bearer Authentication (auth_token):
```python
import openapi_client
from openapi_client.apis.tags import releases_api
from pprint import pprint
# Defining the host is optional and defaults to https://sentry.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://sentry.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: auth_token
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = releases_api.ReleasesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'organization_slug': "organization_slug_example",
        'project_slug': "project_slug_example",
        'version': "version_example",
    }
    try:
        api_response = api_instance.list_a_projects_release_files(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ReleasesApi->list_a_projects_release_files: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
organization_slug | OrganizationSlugSchema | | 
project_slug | ProjectSlugSchema | | 
version | VersionSchema | | 

# OrganizationSlugSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ProjectSlugSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_a_projects_release_files.ApiResponseFor200) | Success
403 | [ApiResponseFor403](#list_a_projects_release_files.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#list_a_projects_release_files.ApiResponseFor404) | Not Found

#### list_a_projects_release_files.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**sha1** | str,  | str,  |  | 
**[headers](#headers)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 
**dateCreated** | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time
**size** | decimal.Decimal, int,  | decimal.Decimal,  |  | 
**name** | str,  | str,  |  | 
**dist** | None, str,  | NoneClass, str,  |  | 
**id** | str,  | str,  |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# headers

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

#### list_a_projects_release_files.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### list_a_projects_release_files.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[auth_token](../../../README.md#auth_token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_a_releases_deploys**
<a id="list_a_releases_deploys"></a>
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] list_a_releases_deploys(organization_slugversion)



Return a list of deploys for a given release.

### Example

* Bearer Authentication (auth_token):
```python
import openapi_client
from openapi_client.apis.tags import releases_api
from pprint import pprint
# Defining the host is optional and defaults to https://sentry.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://sentry.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: auth_token
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = releases_api.ReleasesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'organization_slug': "organization_slug_example",
        'version': "version_example",
    }
    try:
        api_response = api_instance.list_a_releases_deploys(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ReleasesApi->list_a_releases_deploys: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
organization_slug | OrganizationSlugSchema | | 
version | VersionSchema | | 

# OrganizationSlugSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_a_releases_deploys.ApiResponseFor200) | Success
403 | [ApiResponseFor403](#list_a_releases_deploys.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#list_a_releases_deploys.ApiResponseFor404) | Not Found

#### list_a_releases_deploys.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**environment** | str,  | str,  |  | 
**dateStarted** | None, str, datetime,  | NoneClass, str,  |  | value must conform to RFC-3339 date-time
**dateFinished** | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time
**name** | None, str,  | NoneClass, str,  |  | 
**id** | str,  | str,  |  | 
**url** | None, str,  | NoneClass, str,  |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### list_a_releases_deploys.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### list_a_releases_deploys.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[auth_token](../../../README.md#auth_token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_an_organization_releases_commits**
<a id="list_an_organization_releases_commits"></a>
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] list_an_organization_releases_commits(organization_slugversion)



List an organization release's commits.

### Example

* Bearer Authentication (auth_token):
```python
import openapi_client
from openapi_client.apis.tags import releases_api
from pprint import pprint
# Defining the host is optional and defaults to https://sentry.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://sentry.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: auth_token
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = releases_api.ReleasesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'organization_slug': "organization_slug_example",
        'version': "version_example",
    }
    try:
        api_response = api_instance.list_an_organization_releases_commits(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ReleasesApi->list_an_organization_releases_commits: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
organization_slug | OrganizationSlugSchema | | 
version | VersionSchema | | 

# OrganizationSlugSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_an_organization_releases_commits.ApiResponseFor200) | Success
403 | [ApiResponseFor403](#list_an_organization_releases_commits.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#list_an_organization_releases_commits.ApiResponseFor404) | Not Found

#### list_an_organization_releases_commits.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**dateCreated** | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time
**id** | str,  | str,  |  | 
**message** | None, str,  | NoneClass, str,  |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### list_an_organization_releases_commits.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### list_an_organization_releases_commits.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[auth_token](../../../README.md#auth_token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_an_organizations_release_files**
<a id="list_an_organizations_release_files"></a>
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] list_an_organizations_release_files(organization_slugversion)



Return a list of files for a given release.

### Example

* Bearer Authentication (auth_token):
```python
import openapi_client
from openapi_client.apis.tags import releases_api
from pprint import pprint
# Defining the host is optional and defaults to https://sentry.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://sentry.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: auth_token
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = releases_api.ReleasesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'organization_slug': "organization_slug_example",
        'version': "version_example",
    }
    try:
        api_response = api_instance.list_an_organizations_release_files(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ReleasesApi->list_an_organizations_release_files: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
organization_slug | OrganizationSlugSchema | | 
version | VersionSchema | | 

# OrganizationSlugSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_an_organizations_release_files.ApiResponseFor200) | Success
403 | [ApiResponseFor403](#list_an_organizations_release_files.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#list_an_organizations_release_files.ApiResponseFor404) | Not Found

#### list_an_organizations_release_files.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**sha1** | str,  | str,  |  | 
**[headers](#headers)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 
**dateCreated** | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time
**size** | decimal.Decimal, int,  | decimal.Decimal,  |  | 
**name** | str,  | str,  |  | 
**dist** | None, str,  | NoneClass, str,  |  | 
**id** | str,  | str,  |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# headers

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

#### list_an_organizations_release_files.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### list_an_organizations_release_files.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[auth_token](../../../README.md#auth_token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_an_organizations_releases**
<a id="list_an_organizations_releases"></a>
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] list_an_organizations_releases(organization_slug)



Return a list of releases for a given organization.

### Example

* Bearer Authentication (auth_token):
```python
import openapi_client
from openapi_client.apis.tags import releases_api
from pprint import pprint
# Defining the host is optional and defaults to https://sentry.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://sentry.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: auth_token
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = releases_api.ReleasesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'organization_slug': "organization_slug_example",
    }
    query_params = {
    }
    try:
        api_response = api_instance.list_an_organizations_releases(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ReleasesApi->list_an_organizations_releases: %s\n" % e)

    # example passing only optional values
    path_params = {
        'organization_slug': "organization_slug_example",
    }
    query_params = {
        'query': "query_example",
    }
    try:
        api_response = api_instance.list_an_organizations_releases(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ReleasesApi->list_an_organizations_releases: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query | QuerySchema | | optional


# QuerySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
organization_slug | OrganizationSlugSchema | | 

# OrganizationSlugSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_an_organizations_releases.ApiResponseFor200) | Success
401 | [ApiResponseFor401](#list_an_organizations_releases.ApiResponseFor401) | Permission Denied
403 | [ApiResponseFor403](#list_an_organizations_releases.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#list_an_organizations_releases.ApiResponseFor404) | Not Found

#### list_an_organizations_releases.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[owner](#owner)** | dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  |  | 
**shortVersion** | str,  | str,  |  | 
**[projects](#projects)** | list, tuple,  | tuple,  |  | 
**[data](#data)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 
**commitCount** | decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer
**[lastCommit](#lastCommit)** | dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  |  | 
**[lastDeploy](#lastDeploy)** | dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  |  | 
**version** | str,  | str,  |  | 
**url** | None, str,  | NoneClass, str,  |  | 
**newGroups** | decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer
**ref** | None, str,  | NoneClass, str,  |  | 
**dateCreated** | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time
**firstEvent** | None, str, datetime,  | NoneClass, str,  |  | value must conform to RFC-3339 date-time
**lastEvent** | None, str, datetime,  | NoneClass, str,  |  | value must conform to RFC-3339 date-time
**deployCount** | decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer
**dateReleased** | None, str, datetime,  | NoneClass, str,  |  | value must conform to RFC-3339 date-time
**[authors](#authors)** | list, tuple,  | tuple,  |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# authors

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# data

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# lastCommit

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  |  | 

# lastDeploy

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### oneOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[one_of_0](#one_of_0) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 
[one_of_1](#one_of_1) | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

# one_of_0

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**environment** | str,  | str,  |  | 
**dateStarted** | None, str, datetime,  | NoneClass, str,  |  | value must conform to RFC-3339 date-time
**dateFinished** | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time
**name** | None, str,  | NoneClass, str,  |  | 
**id** | str,  | str,  |  | 
**url** | None, str,  | NoneClass, str,  |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# one_of_1

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### not
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[not_schema](#not_schema) | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

# not_schema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### anyOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[any_of_0](#any_of_0) | str,  | str,  |  | 
[any_of_1](#any_of_1) | decimal.Decimal, int, float,  | decimal.Decimal,  |  | 
[any_of_2](#any_of_2) | bool,  | BoolClass,  |  | 
[any_of_3](#any_of_3) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 
[any_of_4](#any_of_4) | list, tuple,  | tuple,  |  | 

# any_of_0

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# any_of_1

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  |  | 

# any_of_2

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# any_of_3

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# any_of_4

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

# owner

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  |  | 

# projects

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  |  | [optional] 
**slug** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### list_an_organizations_releases.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### list_an_organizations_releases.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### list_an_organizations_releases.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[auth_token](../../../README.md#auth_token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_issues_to_be_resolved_in_a_particular_release**
<a id="list_issues_to_be_resolved_in_a_particular_release"></a>
> list_issues_to_be_resolved_in_a_particular_release(organization_slugproject_slugversion)



List issues to be resolved in a particular release.

### Example

* Bearer Authentication (auth_token):
```python
import openapi_client
from openapi_client.apis.tags import releases_api
from pprint import pprint
# Defining the host is optional and defaults to https://sentry.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://sentry.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: auth_token
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = releases_api.ReleasesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'organization_slug': "organization_slug_example",
        'project_slug': "project_slug_example",
        'version': "version_example",
    }
    try:
        api_response = api_instance.list_issues_to_be_resolved_in_a_particular_release(
            path_params=path_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling ReleasesApi->list_issues_to_be_resolved_in_a_particular_release: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
organization_slug | OrganizationSlugSchema | | 
project_slug | ProjectSlugSchema | | 
version | VersionSchema | | 

# OrganizationSlugSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ProjectSlugSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_issues_to_be_resolved_in_a_particular_release.ApiResponseFor200) | Success
403 | [ApiResponseFor403](#list_issues_to_be_resolved_in_a_particular_release.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#list_issues_to_be_resolved_in_a_particular_release.ApiResponseFor404) | Not Found

#### list_issues_to_be_resolved_in_a_particular_release.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### list_issues_to_be_resolved_in_a_particular_release.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### list_issues_to_be_resolved_in_a_particular_release.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[auth_token](../../../README.md#auth_token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **retrieve_a_project_releases_file**
<a id="retrieve_a_project_releases_file"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} retrieve_a_project_releases_file(organization_slugproject_slugversionfile_id)



Retrieve a file for a given release.

### Example

* Bearer Authentication (auth_token):
```python
import openapi_client
from openapi_client.apis.tags import releases_api
from pprint import pprint
# Defining the host is optional and defaults to https://sentry.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://sentry.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: auth_token
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = releases_api.ReleasesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'organization_slug': "organization_slug_example",
        'project_slug': "project_slug_example",
        'version': "version_example",
        'file_id': "file_id_example",
    }
    query_params = {
    }
    try:
        api_response = api_instance.retrieve_a_project_releases_file(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ReleasesApi->retrieve_a_project_releases_file: %s\n" % e)

    # example passing only optional values
    path_params = {
        'organization_slug': "organization_slug_example",
        'project_slug': "project_slug_example",
        'version': "version_example",
        'file_id': "file_id_example",
    }
    query_params = {
        'download': True,
    }
    try:
        api_response = api_instance.retrieve_a_project_releases_file(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ReleasesApi->retrieve_a_project_releases_file: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
download | DownloadSchema | | optional


# DownloadSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
organization_slug | OrganizationSlugSchema | | 
project_slug | ProjectSlugSchema | | 
version | VersionSchema | | 
file_id | FileIdSchema | | 

# OrganizationSlugSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ProjectSlugSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FileIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#retrieve_a_project_releases_file.ApiResponseFor200) | Success
403 | [ApiResponseFor403](#retrieve_a_project_releases_file.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#retrieve_a_project_releases_file.ApiResponseFor404) | Not Found

#### retrieve_a_project_releases_file.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**sha1** | str,  | str,  |  | 
**[headers](#headers)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 
**dateCreated** | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time
**size** | decimal.Decimal, int,  | decimal.Decimal,  |  | 
**name** | str,  | str,  |  | 
**dist** | None, str,  | NoneClass, str,  |  | 
**id** | str,  | str,  |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# headers

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

#### retrieve_a_project_releases_file.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### retrieve_a_project_releases_file.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[auth_token](../../../README.md#auth_token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **retrieve_an_organization_releases_file**
<a id="retrieve_an_organization_releases_file"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} retrieve_an_organization_releases_file(organization_slugversionfile_id)



Retrieve a file for a given release.

### Example

* Bearer Authentication (auth_token):
```python
import openapi_client
from openapi_client.apis.tags import releases_api
from pprint import pprint
# Defining the host is optional and defaults to https://sentry.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://sentry.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: auth_token
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = releases_api.ReleasesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'organization_slug': "organization_slug_example",
        'version': "version_example",
        'file_id': "file_id_example",
    }
    query_params = {
    }
    try:
        api_response = api_instance.retrieve_an_organization_releases_file(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ReleasesApi->retrieve_an_organization_releases_file: %s\n" % e)

    # example passing only optional values
    path_params = {
        'organization_slug': "organization_slug_example",
        'version': "version_example",
        'file_id': "file_id_example",
    }
    query_params = {
        'download': True,
    }
    try:
        api_response = api_instance.retrieve_an_organization_releases_file(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ReleasesApi->retrieve_an_organization_releases_file: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
download | DownloadSchema | | optional


# DownloadSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
organization_slug | OrganizationSlugSchema | | 
version | VersionSchema | | 
file_id | FileIdSchema | | 

# OrganizationSlugSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FileIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#retrieve_an_organization_releases_file.ApiResponseFor200) | Success
403 | [ApiResponseFor403](#retrieve_an_organization_releases_file.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#retrieve_an_organization_releases_file.ApiResponseFor404) | Not Found

#### retrieve_an_organization_releases_file.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**sha1** | str,  | str,  |  | 
**[headers](#headers)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 
**dateCreated** | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time
**size** | decimal.Decimal, int,  | decimal.Decimal,  |  | 
**name** | str,  | str,  |  | 
**dist** | None, str,  | NoneClass, str,  |  | 
**id** | str,  | str,  |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# headers

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

#### retrieve_an_organization_releases_file.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### retrieve_an_organization_releases_file.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[auth_token](../../../README.md#auth_token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **retrieve_an_organizations_releases**
<a id="retrieve_an_organizations_releases"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} retrieve_an_organizations_releases(organization_slugversion)



Return a release for a given organization.

### Example

* Bearer Authentication (auth_token):
```python
import openapi_client
from openapi_client.apis.tags import releases_api
from pprint import pprint
# Defining the host is optional and defaults to https://sentry.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://sentry.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: auth_token
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = releases_api.ReleasesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'organization_slug': "organization_slug_example",
        'version': "version_example",
    }
    try:
        api_response = api_instance.retrieve_an_organizations_releases(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ReleasesApi->retrieve_an_organizations_releases: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
organization_slug | OrganizationSlugSchema | | 
version | VersionSchema | | 

# OrganizationSlugSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#retrieve_an_organizations_releases.ApiResponseFor200) | Success
403 | [ApiResponseFor403](#retrieve_an_organizations_releases.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#retrieve_an_organizations_releases.ApiResponseFor404) | Not Found

#### retrieve_an_organizations_releases.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[owner](#owner)** | dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  |  | 
**shortVersion** | str,  | str,  |  | 
**[projects](#projects)** | list, tuple,  | tuple,  |  | 
**[data](#data)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 
**commitCount** | decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer
**[lastCommit](#lastCommit)** | dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  |  | 
**[lastDeploy](#lastDeploy)** | dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  |  | 
**version** | str,  | str,  |  | 
**url** | None, str,  | NoneClass, str,  |  | 
**newGroups** | decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer
**ref** | None, str,  | NoneClass, str,  |  | 
**dateCreated** | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time
**firstEvent** | None, str, datetime,  | NoneClass, str,  |  | value must conform to RFC-3339 date-time
**lastEvent** | None, str, datetime,  | NoneClass, str,  |  | value must conform to RFC-3339 date-time
**deployCount** | decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer
**dateReleased** | None, str, datetime,  | NoneClass, str,  |  | value must conform to RFC-3339 date-time
**[authors](#authors)** | list, tuple,  | tuple,  |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# authors

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# data

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# lastCommit

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  |  | 

# lastDeploy

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### oneOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[one_of_0](#one_of_0) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 
[one_of_1](#one_of_1) | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

# one_of_0

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**environment** | str,  | str,  |  | 
**dateStarted** | None, str, datetime,  | NoneClass, str,  |  | value must conform to RFC-3339 date-time
**dateFinished** | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time
**name** | None, str,  | NoneClass, str,  |  | 
**id** | str,  | str,  |  | 
**url** | None, str,  | NoneClass, str,  |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# one_of_1

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### not
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[not_schema](#not_schema) | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

# not_schema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### anyOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[any_of_0](#any_of_0) | str,  | str,  |  | 
[any_of_1](#any_of_1) | decimal.Decimal, int, float,  | decimal.Decimal,  |  | 
[any_of_2](#any_of_2) | bool,  | BoolClass,  |  | 
[any_of_3](#any_of_3) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 
[any_of_4](#any_of_4) | list, tuple,  | tuple,  |  | 

# any_of_0

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# any_of_1

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  |  | 

# any_of_2

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# any_of_3

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# any_of_4

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

# owner

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  |  | 

# projects

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  |  | [optional] 
**slug** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### retrieve_an_organizations_releases.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### retrieve_an_organizations_releases.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[auth_token](../../../README.md#auth_token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **retrieve_files_changed_in_a_releases_commits**
<a id="retrieve_files_changed_in_a_releases_commits"></a>
> retrieve_files_changed_in_a_releases_commits(organization_slugversion)



Retrieve files changed in a release's commits

### Example

* Bearer Authentication (auth_token):
```python
import openapi_client
from openapi_client.apis.tags import releases_api
from pprint import pprint
# Defining the host is optional and defaults to https://sentry.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://sentry.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: auth_token
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = releases_api.ReleasesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'organization_slug': "organization_slug_example",
        'version': "version_example",
    }
    try:
        api_response = api_instance.retrieve_files_changed_in_a_releases_commits(
            path_params=path_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling ReleasesApi->retrieve_files_changed_in_a_releases_commits: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
organization_slug | OrganizationSlugSchema | | 
version | VersionSchema | | 

# OrganizationSlugSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#retrieve_files_changed_in_a_releases_commits.ApiResponseFor200) | Success
403 | [ApiResponseFor403](#retrieve_files_changed_in_a_releases_commits.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#retrieve_files_changed_in_a_releases_commits.ApiResponseFor404) | Not Found

#### retrieve_files_changed_in_a_releases_commits.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### retrieve_files_changed_in_a_releases_commits.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### retrieve_files_changed_in_a_releases_commits.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[auth_token](../../../README.md#auth_token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **retrieve_release_health_session_statistics**
<a id="retrieve_release_health_session_statistics"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} retrieve_release_health_session_statistics(organization_slugprojectfield)



Returns a time series of release health session statistics for projects bound to an organization.  The interval and date range are subject to certain restrictions and rounding rules.  The date range is rounded to align with the interval, and is rounded to at least one hour. The interval can at most be one day and at least one hour currently. It has to cleanly divide one day, for rounding reasons.  Apart from the query parameters listed below, this endpoint also supports the usual [pagination parameters](https://docs.sentry.io/api/pagination/).

### Example

* Bearer Authentication (auth_token):
```python
import openapi_client
from openapi_client.apis.tags import releases_api
from pprint import pprint
# Defining the host is optional and defaults to https://sentry.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://sentry.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: auth_token
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = releases_api.ReleasesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'organization_slug': "organization_slug_example",
    }
    query_params = {
        'project': [
        1
    ],
        'field': [
        "field_example"
    ],
    }
    try:
        api_response = api_instance.retrieve_release_health_session_statistics(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ReleasesApi->retrieve_release_health_session_statistics: %s\n" % e)

    # example passing only optional values
    path_params = {
        'organization_slug': "organization_slug_example",
    }
    query_params = {
        'project': [
        1
    ],
        'field': [
        "field_example"
    ],
        'environment': [
        "environment_example"
    ],
        'groupBy': [
        "groupBy_example"
    ],
        'orderBy': "orderBy_example",
        'query': "query_example",
        'statsPeriod': "statsPeriod_example",
        'interval': "interval_example",
        'statsPeriodStart': "statsPeriodStart_example",
        'statsPeriodEnd': "statsPeriodEnd_example",
        'start': "1970-01-01T00:00:00.00Z",
        'end': "1970-01-01T00:00:00.00Z",
    }
    try:
        api_response = api_instance.retrieve_release_health_session_statistics(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ReleasesApi->retrieve_release_health_session_statistics: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
project | ProjectSchema | | 
field | FieldSchema | | 
environment | EnvironmentSchema | | optional
groupBy | GroupBySchema | | optional
orderBy | OrderBySchema | | optional
query | QuerySchema | | optional
statsPeriod | StatsPeriodSchema | | optional
interval | IntervalSchema | | optional
statsPeriodStart | StatsPeriodStartSchema | | optional
statsPeriodEnd | StatsPeriodEndSchema | | optional
start | StartSchema | | optional
end | EndSchema | | optional


# ProjectSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# FieldSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# EnvironmentSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# GroupBySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# OrderBySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# QuerySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# StatsPeriodSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# IntervalSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# StatsPeriodStartSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# StatsPeriodEndSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# StartSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

# EndSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
organization_slug | OrganizationSlugSchema | | 

# OrganizationSlugSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#retrieve_release_health_session_statistics.ApiResponseFor200) | Time-series Session Statistics.
400 | [ApiResponseFor400](#retrieve_release_health_session_statistics.ApiResponseFor400) | Wrong Parameters
401 | [ApiResponseFor401](#retrieve_release_health_session_statistics.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#retrieve_release_health_session_statistics.ApiResponseFor403) | Forbidden

#### retrieve_release_health_session_statistics.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[intervals](#intervals)** | list, tuple,  | tuple,  | The time slices of the timeseries data given in the &#x60;groups[].series&#x60; field. | 
**start** | str, datetime,  | str,  | The start time of the data being returned. | value must conform to RFC-3339 date-time
**[groups](#groups)** | list, tuple,  | tuple,  |  | 
**end** | str, datetime,  | str,  | The exclusive end time of the data being returned. | value must conform to RFC-3339 date-time
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# intervals

The time slices of the timeseries data given in the `groups[].series` field.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The time slices of the timeseries data given in the &#x60;groups[].series&#x60; field. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

# groups

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  | A grouped result, as requested by the &#x60;groupBy&#x60; request parameter. | 

# items

A grouped result, as requested by the `groupBy` request parameter.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A grouped result, as requested by the &#x60;groupBy&#x60; request parameter. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[series](#series)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | These are key/value pairs, the key being the requested &#x60;field&#x60;, and the value is an array of aggregated values. The array corresponds to the times given in the &#x60;intervals&#x60; array. | 
**[by](#by)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | These are key/value pairs, the key being the requested &#x60;groupBy&#x60; property with its corresponding value. | 
**[totals](#totals)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | These are key/value pairs, the key being the requested &#x60;field&#x60;, and the value the corresponding total over the requested time frame. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# by

These are key/value pairs, the key being the requested `groupBy` property with its corresponding value.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | These are key/value pairs, the key being the requested &#x60;groupBy&#x60; property with its corresponding value. | 

# totals

These are key/value pairs, the key being the requested `field`, and the value the corresponding total over the requested time frame.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | These are key/value pairs, the key being the requested &#x60;field&#x60;, and the value the corresponding total over the requested time frame. | 

# series

These are key/value pairs, the key being the requested `field`, and the value is an array of aggregated values. The array corresponds to the times given in the `intervals` array.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | These are key/value pairs, the key being the requested &#x60;field&#x60;, and the value is an array of aggregated values. The array corresponds to the times given in the &#x60;intervals&#x60; array. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[any_string_name](#any_string_name)** | list, tuple,  | tuple,  | any string name can be used but the value must be the correct type | [optional] 

# any_string_name

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

#### retrieve_release_health_session_statistics.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**detail** | str,  | str,  |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### retrieve_release_health_session_statistics.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### retrieve_release_health_session_statistics.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[auth_token](../../../README.md#auth_token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_a_project_release_file**
<a id="update_a_project_release_file"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} update_a_project_release_file(organization_slugproject_slugversionfile_id)



Update a project release file.

### Example

* Bearer Authentication (auth_token):
```python
import openapi_client
from openapi_client.apis.tags import releases_api
from pprint import pprint
# Defining the host is optional and defaults to https://sentry.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://sentry.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: auth_token
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = releases_api.ReleasesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'organization_slug': "organization_slug_example",
        'project_slug': "project_slug_example",
        'version': "version_example",
        'file_id': "file_id_example",
    }
    try:
        api_response = api_instance.update_a_project_release_file(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ReleasesApi->update_a_project_release_file: %s\n" % e)

    # example passing only optional values
    path_params = {
        'organization_slug': "organization_slug_example",
        'project_slug': "project_slug_example",
        'version': "version_example",
        'file_id': "file_id_example",
    }
    body = dict(
        name="name_example",
        dist="dist_example",
    )
    try:
        api_response = api_instance.update_a_project_release_file(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ReleasesApi->update_a_project_release_file: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  | The new name (full path) of the file. | [optional] 
**dist** | str,  | str,  | The new name of the dist. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
organization_slug | OrganizationSlugSchema | | 
project_slug | ProjectSlugSchema | | 
version | VersionSchema | | 
file_id | FileIdSchema | | 

# OrganizationSlugSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ProjectSlugSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FileIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#update_a_project_release_file.ApiResponseFor200) | Success
403 | [ApiResponseFor403](#update_a_project_release_file.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#update_a_project_release_file.ApiResponseFor404) | Not Found

#### update_a_project_release_file.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**sha1** | str,  | str,  |  | 
**[headers](#headers)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 
**dateCreated** | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time
**size** | decimal.Decimal, int,  | decimal.Decimal,  |  | 
**name** | str,  | str,  |  | 
**dist** | None, str,  | NoneClass, str,  |  | 
**id** | str,  | str,  |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# headers

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

#### update_a_project_release_file.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### update_a_project_release_file.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[auth_token](../../../README.md#auth_token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_an_organization_release_file**
<a id="update_an_organization_release_file"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} update_an_organization_release_file(organization_slugversionfile_id)



Update an organization release file.

### Example

* Bearer Authentication (auth_token):
```python
import openapi_client
from openapi_client.apis.tags import releases_api
from pprint import pprint
# Defining the host is optional and defaults to https://sentry.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://sentry.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: auth_token
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = releases_api.ReleasesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'organization_slug': "organization_slug_example",
        'version': "version_example",
        'file_id': "file_id_example",
    }
    try:
        api_response = api_instance.update_an_organization_release_file(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ReleasesApi->update_an_organization_release_file: %s\n" % e)

    # example passing only optional values
    path_params = {
        'organization_slug': "organization_slug_example",
        'version': "version_example",
        'file_id': "file_id_example",
    }
    body = dict(
        name="name_example",
        dist="dist_example",
    )
    try:
        api_response = api_instance.update_an_organization_release_file(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ReleasesApi->update_an_organization_release_file: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  | The new name (full path) of the file. | [optional] 
**dist** | str,  | str,  | The new name of the dist. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
organization_slug | OrganizationSlugSchema | | 
version | VersionSchema | | 
file_id | FileIdSchema | | 

# OrganizationSlugSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FileIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#update_an_organization_release_file.ApiResponseFor200) | Success
403 | [ApiResponseFor403](#update_an_organization_release_file.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#update_an_organization_release_file.ApiResponseFor404) | Not Found

#### update_an_organization_release_file.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**sha1** | str,  | str,  |  | 
**[headers](#headers)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 
**dateCreated** | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time
**size** | decimal.Decimal, int,  | decimal.Decimal,  |  | 
**name** | str,  | str,  |  | 
**dist** | None, str,  | NoneClass, str,  |  | 
**id** | str,  | str,  |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# headers

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

#### update_an_organization_release_file.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### update_an_organization_release_file.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[auth_token](../../../README.md#auth_token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_an_organizations_release**
<a id="update_an_organizations_release"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} update_an_organizations_release(organization_slugversion)



Update a release for a given organization.

### Example

* Bearer Authentication (auth_token):
```python
import openapi_client
from openapi_client.apis.tags import releases_api
from pprint import pprint
# Defining the host is optional and defaults to https://sentry.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://sentry.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: auth_token
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = releases_api.ReleasesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'organization_slug': "organization_slug_example",
        'version': "version_example",
    }
    try:
        api_response = api_instance.update_an_organizations_release(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ReleasesApi->update_an_organizations_release: %s\n" % e)

    # example passing only optional values
    path_params = {
        'organization_slug': "organization_slug_example",
        'version': "version_example",
    }
    body = dict(
        ref="ref_example",
        url="url_example",
        date_released="1970-01-01T00:00:00.00Z",
        commits=[
            dict()
        ],
        refs=[
            dict()
        ],
    )
    try:
        api_response = api_instance.update_an_organizations_release(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ReleasesApi->update_an_organizations_release: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**ref** | str,  | str,  | An optional commit reference. This is useful if a tagged version has been provided. | [optional] 
**url** | str,  | str,  | A URL that points to the release. This can be the path to an online interface to the source code for instance. | [optional] 
**dateReleased** | str, datetime,  | str,  | An optional date that indicates when the release went live. If not provided the current time is assumed. | [optional] value must conform to RFC-3339 date-time
**[commits](#commits)** | list, tuple,  | tuple,  | An optional list of commit data to be associated with the release. Commits must include parameters &#x60;id&#x60; (the sha of the commit), and can optionally include &#x60;repository&#x60;, &#x60;message&#x60;, &#x60;author_name&#x60;, &#x60;author_email&#x60;, and &#x60;timestamp&#x60;. | [optional] 
**[refs](#refs)** | list, tuple,  | tuple,  | An optional way to indicate the start and end commits for each repository included in a release. Head commits must include parameters &#x60;repository&#x60; and &#x60;commit&#x60; (the HEAD sha). They can optionally include &#x60;previousCommit&#x60; (the sha of the HEAD of the previous release), which should be specified if this is the first time you&#x27;ve sent commit data. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# commits

An optional list of commit data to be associated with the release. Commits must include parameters `id` (the sha of the commit), and can optionally include `repository`, `message`, `author_name`, `author_email`, and `timestamp`.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | An optional list of commit data to be associated with the release. Commits must include parameters &#x60;id&#x60; (the sha of the commit), and can optionally include &#x60;repository&#x60;, &#x60;message&#x60;, &#x60;author_name&#x60;, &#x60;author_email&#x60;, and &#x60;timestamp&#x60;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# refs

An optional way to indicate the start and end commits for each repository included in a release. Head commits must include parameters `repository` and `commit` (the HEAD sha). They can optionally include `previousCommit` (the sha of the HEAD of the previous release), which should be specified if this is the first time you've sent commit data.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | An optional way to indicate the start and end commits for each repository included in a release. Head commits must include parameters &#x60;repository&#x60; and &#x60;commit&#x60; (the HEAD sha). They can optionally include &#x60;previousCommit&#x60; (the sha of the HEAD of the previous release), which should be specified if this is the first time you&#x27;ve sent commit data. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
organization_slug | OrganizationSlugSchema | | 
version | VersionSchema | | 

# OrganizationSlugSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#update_an_organizations_release.ApiResponseFor200) | Success
403 | [ApiResponseFor403](#update_an_organizations_release.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#update_an_organizations_release.ApiResponseFor404) | Not Found

#### update_an_organizations_release.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[owner](#owner)** | dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  |  | 
**shortVersion** | str,  | str,  |  | 
**[projects](#projects)** | list, tuple,  | tuple,  |  | 
**[data](#data)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 
**commitCount** | decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer
**[lastCommit](#lastCommit)** | dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  |  | 
**[lastDeploy](#lastDeploy)** | dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  |  | 
**version** | str,  | str,  |  | 
**url** | None, str,  | NoneClass, str,  |  | 
**newGroups** | decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer
**ref** | None, str,  | NoneClass, str,  |  | 
**dateCreated** | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time
**firstEvent** | None, str, datetime,  | NoneClass, str,  |  | value must conform to RFC-3339 date-time
**lastEvent** | None, str, datetime,  | NoneClass, str,  |  | value must conform to RFC-3339 date-time
**deployCount** | decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer
**dateReleased** | None, str, datetime,  | NoneClass, str,  |  | value must conform to RFC-3339 date-time
**[authors](#authors)** | list, tuple,  | tuple,  |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# authors

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# data

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# lastCommit

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  |  | 

# lastDeploy

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### oneOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[one_of_0](#one_of_0) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 
[one_of_1](#one_of_1) | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

# one_of_0

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**environment** | str,  | str,  |  | 
**dateStarted** | None, str, datetime,  | NoneClass, str,  |  | value must conform to RFC-3339 date-time
**dateFinished** | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time
**name** | None, str,  | NoneClass, str,  |  | 
**id** | str,  | str,  |  | 
**url** | None, str,  | NoneClass, str,  |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# one_of_1

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### not
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[not_schema](#not_schema) | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

# not_schema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### anyOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[any_of_0](#any_of_0) | str,  | str,  |  | 
[any_of_1](#any_of_1) | decimal.Decimal, int, float,  | decimal.Decimal,  |  | 
[any_of_2](#any_of_2) | bool,  | BoolClass,  |  | 
[any_of_3](#any_of_3) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 
[any_of_4](#any_of_4) | list, tuple,  | tuple,  |  | 

# any_of_0

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# any_of_1

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  |  | 

# any_of_2

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# any_of_3

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# any_of_4

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

# owner

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  |  | 

# projects

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  |  | [optional] 
**slug** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### update_an_organizations_release.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### update_an_organizations_release.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[auth_token](../../../README.md#auth_token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **upload_a_new_organization_release_file**
<a id="upload_a_new_organization_release_file"></a>
> upload_a_new_organization_release_file(organization_slugversion)



Upload a new organization release file.

### Example

* Bearer Authentication (auth_token):
```python
import openapi_client
from openapi_client.apis.tags import releases_api
from pprint import pprint
# Defining the host is optional and defaults to https://sentry.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://sentry.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: auth_token
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = releases_api.ReleasesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'organization_slug': "organization_slug_example",
        'version': "version_example",
    }
    try:
        api_response = api_instance.upload_a_new_organization_release_file(
            path_params=path_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling ReleasesApi->upload_a_new_organization_release_file: %s\n" % e)

    # example passing only optional values
    path_params = {
        'organization_slug': "organization_slug_example",
        'version': "version_example",
    }
    body = dict(
        name="name_example",
        file=open('/path/to/file', 'rb'),
        dist="dist_example",
        header="header_example",
    )
    try:
        api_response = api_instance.upload_a_new_organization_release_file(
            path_params=path_params,
            body=body,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling ReleasesApi->upload_a_new_organization_release_file: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyMultipartFormData, Unset] | optional, default is unset |
path_params | RequestPathParams | |
content_type | str | optional, default is 'multipart/form-data' | Selects the schema and serialization of the request body
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyMultipartFormData

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**file** | bytes, io.FileIO, io.BufferedReader,  | bytes, FileIO,  | The multipart encoded file. | 
**name** | str,  | str,  | The name (full path) of the file. | [optional] 
**dist** | str,  | str,  | The name of the dist. | [optional] 
**header** | str,  | str,  | This parameter can be supplied multiple times to attach headers to the file. Each header is a string in the format &#x60;key:value&#x60;. For instance it can be used to define a content type. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
organization_slug | OrganizationSlugSchema | | 
version | VersionSchema | | 

# OrganizationSlugSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#upload_a_new_organization_release_file.ApiResponseFor201) | Success
403 | [ApiResponseFor403](#upload_a_new_organization_release_file.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#upload_a_new_organization_release_file.ApiResponseFor404) | Not Found

#### upload_a_new_organization_release_file.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### upload_a_new_organization_release_file.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### upload_a_new_organization_release_file.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[auth_token](../../../README.md#auth_token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **upload_a_new_project_release_file**
<a id="upload_a_new_project_release_file"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} upload_a_new_project_release_file(organization_slugproject_slugversion)



Upload a new project release file.

### Example

* Bearer Authentication (auth_token):
```python
import openapi_client
from openapi_client.apis.tags import releases_api
from pprint import pprint
# Defining the host is optional and defaults to https://sentry.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://sentry.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: auth_token
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = releases_api.ReleasesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'organization_slug': "organization_slug_example",
        'project_slug': "project_slug_example",
        'version': "version_example",
    }
    try:
        api_response = api_instance.upload_a_new_project_release_file(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ReleasesApi->upload_a_new_project_release_file: %s\n" % e)

    # example passing only optional values
    path_params = {
        'organization_slug': "organization_slug_example",
        'project_slug': "project_slug_example",
        'version': "version_example",
    }
    body = dict(
        name="name_example",
        file=open('/path/to/file', 'rb'),
        dist="dist_example",
        header="header_example",
    )
    try:
        api_response = api_instance.upload_a_new_project_release_file(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ReleasesApi->upload_a_new_project_release_file: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyMultipartFormData, Unset] | optional, default is unset |
path_params | RequestPathParams | |
content_type | str | optional, default is 'multipart/form-data' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyMultipartFormData

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**file** | bytes, io.FileIO, io.BufferedReader,  | bytes, FileIO,  | The multipart encoded file. | 
**name** | str,  | str,  | The name (full path) of the file. | [optional] 
**dist** | str,  | str,  | The name of the dist. | [optional] 
**header** | str,  | str,  | This parameter can be supplied multiple times to attach headers to the file. Each header is a string in the format &#x60;key:value&#x60;. For instance it can be used to define a content type. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
organization_slug | OrganizationSlugSchema | | 
project_slug | ProjectSlugSchema | | 
version | VersionSchema | | 

# OrganizationSlugSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ProjectSlugSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#upload_a_new_project_release_file.ApiResponseFor201) | Success
403 | [ApiResponseFor403](#upload_a_new_project_release_file.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#upload_a_new_project_release_file.ApiResponseFor404) | Not Found

#### upload_a_new_project_release_file.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**sha1** | str,  | str,  |  | 
**[headers](#headers)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 
**dateCreated** | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time
**size** | decimal.Decimal, int,  | decimal.Decimal,  |  | 
**name** | str,  | str,  |  | 
**dist** | None, str,  | NoneClass, str,  |  | 
**id** | str,  | str,  |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# headers

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

#### upload_a_new_project_release_file.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### upload_a_new_project_release_file.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[auth_token](../../../README.md#auth_token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

