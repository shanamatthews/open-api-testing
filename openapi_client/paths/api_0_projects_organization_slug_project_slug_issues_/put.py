# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from urllib3._collections import HTTPHeaderDict

from openapi_client import api_client, exceptions
from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from openapi_client import schemas  # noqa: F401

from . import path

# Query params
IdSchema = schemas.IntSchema
StatusSchema = schemas.StrSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'id': typing.Union[IdSchema, decimal.Decimal, int, ],
        'status': typing.Union[StatusSchema, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_id = api_client.QueryParameter(
    name="id",
    style=api_client.ParameterStyle.FORM,
    schema=IdSchema,
    explode=True,
)
request_query_status = api_client.QueryParameter(
    name="status",
    style=api_client.ParameterStyle.FORM,
    schema=StatusSchema,
    explode=True,
)
# Path params
OrganizationSlugSchema = schemas.StrSchema
ProjectSlugSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'organization_slug': typing.Union[OrganizationSlugSchema, str, ],
        'project_slug': typing.Union[ProjectSlugSchema, str, ],
    }
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_organization_slug = api_client.PathParameter(
    name="organization_slug",
    style=api_client.ParameterStyle.SIMPLE,
    schema=OrganizationSlugSchema,
    required=True,
)
request_path_project_slug = api_client.PathParameter(
    name="project_slug",
    style=api_client.ParameterStyle.SIMPLE,
    schema=ProjectSlugSchema,
    required=True,
)
# body param


class SchemaForRequestBodyApplicationJson(
    schemas.DictSchema
):


    class MetaOapg:
        
        class properties:
            status = schemas.StrSchema
            
            
            class statusDetails(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    class properties:
                        inRelease = schemas.StrSchema
                        inNextRelease = schemas.BoolSchema
                        inCommit = schemas.StrSchema
                        ignoreDuration = schemas.IntSchema
                        ignoreCount = schemas.IntSchema
                        ignoreWindow = schemas.IntSchema
                        ignoreUserCount = schemas.IntSchema
                        ignoreUserWindow = schemas.IntSchema
                        __annotations__ = {
                            "inRelease": inRelease,
                            "inNextRelease": inNextRelease,
                            "inCommit": inCommit,
                            "ignoreDuration": ignoreDuration,
                            "ignoreCount": ignoreCount,
                            "ignoreWindow": ignoreWindow,
                            "ignoreUserCount": ignoreUserCount,
                            "ignoreUserWindow": ignoreUserWindow,
                        }
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["inRelease"]) -> MetaOapg.properties.inRelease: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["inNextRelease"]) -> MetaOapg.properties.inNextRelease: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["inCommit"]) -> MetaOapg.properties.inCommit: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["ignoreDuration"]) -> MetaOapg.properties.ignoreDuration: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["ignoreCount"]) -> MetaOapg.properties.ignoreCount: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["ignoreWindow"]) -> MetaOapg.properties.ignoreWindow: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["ignoreUserCount"]) -> MetaOapg.properties.ignoreUserCount: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["ignoreUserWindow"]) -> MetaOapg.properties.ignoreUserWindow: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["inRelease", "inNextRelease", "inCommit", "ignoreDuration", "ignoreCount", "ignoreWindow", "ignoreUserCount", "ignoreUserWindow", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["inRelease"]) -> typing.Union[MetaOapg.properties.inRelease, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["inNextRelease"]) -> typing.Union[MetaOapg.properties.inNextRelease, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["inCommit"]) -> typing.Union[MetaOapg.properties.inCommit, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["ignoreDuration"]) -> typing.Union[MetaOapg.properties.ignoreDuration, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["ignoreCount"]) -> typing.Union[MetaOapg.properties.ignoreCount, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["ignoreWindow"]) -> typing.Union[MetaOapg.properties.ignoreWindow, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["ignoreUserCount"]) -> typing.Union[MetaOapg.properties.ignoreUserCount, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["ignoreUserWindow"]) -> typing.Union[MetaOapg.properties.ignoreUserWindow, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["inRelease", "inNextRelease", "inCommit", "ignoreDuration", "ignoreCount", "ignoreWindow", "ignoreUserCount", "ignoreUserWindow", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    inRelease: typing.Union[MetaOapg.properties.inRelease, str, schemas.Unset] = schemas.unset,
                    inNextRelease: typing.Union[MetaOapg.properties.inNextRelease, bool, schemas.Unset] = schemas.unset,
                    inCommit: typing.Union[MetaOapg.properties.inCommit, str, schemas.Unset] = schemas.unset,
                    ignoreDuration: typing.Union[MetaOapg.properties.ignoreDuration, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                    ignoreCount: typing.Union[MetaOapg.properties.ignoreCount, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                    ignoreWindow: typing.Union[MetaOapg.properties.ignoreWindow, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                    ignoreUserCount: typing.Union[MetaOapg.properties.ignoreUserCount, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                    ignoreUserWindow: typing.Union[MetaOapg.properties.ignoreUserWindow, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'statusDetails':
                    return super().__new__(
                        cls,
                        *_args,
                        inRelease=inRelease,
                        inNextRelease=inNextRelease,
                        inCommit=inCommit,
                        ignoreDuration=ignoreDuration,
                        ignoreCount=ignoreCount,
                        ignoreWindow=ignoreWindow,
                        ignoreUserCount=ignoreUserCount,
                        ignoreUserWindow=ignoreUserWindow,
                        _configuration=_configuration,
                        **kwargs,
                    )
            ignoreDuration = schemas.IntSchema
            isPublic = schemas.BoolSchema
            merge = schemas.BoolSchema
            assignedTo = schemas.StrSchema
            hasSeen = schemas.BoolSchema
            isBookmarked = schemas.BoolSchema
            __annotations__ = {
                "status": status,
                "statusDetails": statusDetails,
                "ignoreDuration": ignoreDuration,
                "isPublic": isPublic,
                "merge": merge,
                "assignedTo": assignedTo,
                "hasSeen": hasSeen,
                "isBookmarked": isBookmarked,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["statusDetails"]) -> MetaOapg.properties.statusDetails: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ignoreDuration"]) -> MetaOapg.properties.ignoreDuration: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isPublic"]) -> MetaOapg.properties.isPublic: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["merge"]) -> MetaOapg.properties.merge: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["assignedTo"]) -> MetaOapg.properties.assignedTo: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hasSeen"]) -> MetaOapg.properties.hasSeen: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isBookmarked"]) -> MetaOapg.properties.isBookmarked: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["status", "statusDetails", "ignoreDuration", "isPublic", "merge", "assignedTo", "hasSeen", "isBookmarked", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["statusDetails"]) -> typing.Union[MetaOapg.properties.statusDetails, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ignoreDuration"]) -> typing.Union[MetaOapg.properties.ignoreDuration, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isPublic"]) -> typing.Union[MetaOapg.properties.isPublic, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["merge"]) -> typing.Union[MetaOapg.properties.merge, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["assignedTo"]) -> typing.Union[MetaOapg.properties.assignedTo, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hasSeen"]) -> typing.Union[MetaOapg.properties.hasSeen, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isBookmarked"]) -> typing.Union[MetaOapg.properties.isBookmarked, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["status", "statusDetails", "ignoreDuration", "isPublic", "merge", "assignedTo", "hasSeen", "isBookmarked", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        statusDetails: typing.Union[MetaOapg.properties.statusDetails, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        ignoreDuration: typing.Union[MetaOapg.properties.ignoreDuration, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        isPublic: typing.Union[MetaOapg.properties.isPublic, bool, schemas.Unset] = schemas.unset,
        merge: typing.Union[MetaOapg.properties.merge, bool, schemas.Unset] = schemas.unset,
        assignedTo: typing.Union[MetaOapg.properties.assignedTo, str, schemas.Unset] = schemas.unset,
        hasSeen: typing.Union[MetaOapg.properties.hasSeen, bool, schemas.Unset] = schemas.unset,
        isBookmarked: typing.Union[MetaOapg.properties.isBookmarked, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SchemaForRequestBodyApplicationJson':
        return super().__new__(
            cls,
            *_args,
            status=status,
            statusDetails=statusDetails,
            ignoreDuration=ignoreDuration,
            isPublic=isPublic,
            merge=merge,
            assignedTo=assignedTo,
            hasSeen=hasSeen,
            isBookmarked=isBookmarked,
            _configuration=_configuration,
            **kwargs,
        )


request_body_any_type = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
_auth = [
    'auth_token',
]


class SchemaFor200ResponseBodyApplicationJson(
    schemas.DictSchema
):


    class MetaOapg:
        required = {
            "isPublic",
            "statusDetails",
            "status",
        }
        
        class properties:
            isPublic = schemas.BoolSchema
            
            
            class status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "resolved": "RESOLVED",
                        "unresolved": "UNRESOLVED",
                        "ignored": "IGNORED",
                    }
                
                @schemas.classproperty
                def RESOLVED(cls):
                    return cls("resolved")
                
                @schemas.classproperty
                def UNRESOLVED(cls):
                    return cls("unresolved")
                
                @schemas.classproperty
                def IGNORED(cls):
                    return cls("ignored")
            statusDetails = schemas.DictSchema
            __annotations__ = {
                "isPublic": isPublic,
                "status": status,
                "statusDetails": statusDetails,
            }
    
    isPublic: MetaOapg.properties.isPublic
    statusDetails: MetaOapg.properties.statusDetails
    status: MetaOapg.properties.status
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isPublic"]) -> MetaOapg.properties.isPublic: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["statusDetails"]) -> MetaOapg.properties.statusDetails: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["isPublic", "status", "statusDetails", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isPublic"]) -> MetaOapg.properties.isPublic: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["statusDetails"]) -> MetaOapg.properties.statusDetails: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["isPublic", "status", "statusDetails", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        isPublic: typing.Union[MetaOapg.properties.isPublic, bool, ],
        statusDetails: typing.Union[MetaOapg.properties.statusDetails, dict, frozendict.frozendict, ],
        status: typing.Union[MetaOapg.properties.status, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SchemaFor200ResponseBodyApplicationJson':
        return super().__new__(
            cls,
            *_args,
            isPublic=isPublic,
            statusDetails=statusDetails,
            status=status,
            _configuration=_configuration,
            **kwargs,
        )


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor200ResponseBodyApplicationJson,
    ]
    headers: schemas.Unset = schemas.unset


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: schemas.Unset = schemas.unset
    headers: schemas.Unset = schemas.unset


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
)


@dataclass
class ApiResponseFor403(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: schemas.Unset = schemas.unset
    headers: schemas.Unset = schemas.unset


_response_for_403 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor403,
)


@dataclass
class ApiResponseFor404(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: schemas.Unset = schemas.unset
    headers: schemas.Unset = schemas.unset


_response_for_404 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor404,
)
_status_code_to_response = {
    '200': _response_for_200,
    '400': _response_for_400,
    '403': _response_for_403,
    '404': _response_for_404,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):
    @typing.overload
    def _bulk_mutate_a_list_of_issues_oapg(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,dict, frozendict.frozendict, ],
        content_type: typing_extensions.Literal["application/json"] = ...,
        query_params: RequestQueryParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def _bulk_mutate_a_list_of_issues_oapg(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,dict, frozendict.frozendict, ],
        content_type: str = ...,
        query_params: RequestQueryParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...


    @typing.overload
    def _bulk_mutate_a_list_of_issues_oapg(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,dict, frozendict.frozendict, ],
        skip_deserialization: typing_extensions.Literal[True],
        content_type: str = ...,
        query_params: RequestQueryParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def _bulk_mutate_a_list_of_issues_oapg(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,dict, frozendict.frozendict, ],
        content_type: str = ...,
        query_params: RequestQueryParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def _bulk_mutate_a_list_of_issues_oapg(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,dict, frozendict.frozendict, ],
        content_type: str = 'application/json',
        query_params: RequestQueryParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        """
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value

        _path_params = {}
        for parameter in (
            request_path_organization_slug,
            request_path_project_slug,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)

        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)

        prefix_separator_iterator = None
        for parameter in (
            request_query_id,
            request_query_status,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value

        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)

        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        serialized_data = request_body_any_type.serialize(body, content_type)
        _headers.add('Content-Type', content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
        response = self.api_client.call_api(
            resource_path=used_path,
            method='put'.upper(),
            headers=_headers,
            fields=_fields,
            body=_body,
            auth_settings=_auth,
            stream=stream,
            timeout=timeout,
        )

        if skip_deserialization:
            api_response = api_client.ApiResponseWithoutDeserialization(response=response)
        else:
            response_for_status = _status_code_to_response.get(str(response.status))
            if response_for_status:
                api_response = response_for_status.deserialize(response, self.api_client.configuration)
            else:
                api_response = api_client.ApiResponseWithoutDeserialization(response=response)

        if not 200 <= response.status <= 299:
            raise exceptions.ApiException(
                status=response.status,
                reason=response.reason,
                api_response=api_response
            )

        return api_response


class BulkMutateAListOfIssues(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    @typing.overload
    def bulk_mutate_a_list_of_issues(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,dict, frozendict.frozendict, ],
        content_type: typing_extensions.Literal["application/json"] = ...,
        query_params: RequestQueryParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def bulk_mutate_a_list_of_issues(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,dict, frozendict.frozendict, ],
        content_type: str = ...,
        query_params: RequestQueryParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...


    @typing.overload
    def bulk_mutate_a_list_of_issues(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,dict, frozendict.frozendict, ],
        skip_deserialization: typing_extensions.Literal[True],
        content_type: str = ...,
        query_params: RequestQueryParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def bulk_mutate_a_list_of_issues(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,dict, frozendict.frozendict, ],
        content_type: str = ...,
        query_params: RequestQueryParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def bulk_mutate_a_list_of_issues(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,dict, frozendict.frozendict, ],
        content_type: str = 'application/json',
        query_params: RequestQueryParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._bulk_mutate_a_list_of_issues_oapg(
            body=body,
            query_params=query_params,
            path_params=path_params,
            content_type=content_type,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


class ApiForput(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    @typing.overload
    def put(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,dict, frozendict.frozendict, ],
        content_type: typing_extensions.Literal["application/json"] = ...,
        query_params: RequestQueryParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def put(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,dict, frozendict.frozendict, ],
        content_type: str = ...,
        query_params: RequestQueryParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...


    @typing.overload
    def put(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,dict, frozendict.frozendict, ],
        skip_deserialization: typing_extensions.Literal[True],
        content_type: str = ...,
        query_params: RequestQueryParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def put(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,dict, frozendict.frozendict, ],
        content_type: str = ...,
        query_params: RequestQueryParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def put(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,dict, frozendict.frozendict, ],
        content_type: str = 'application/json',
        query_params: RequestQueryParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._bulk_mutate_a_list_of_issues_oapg(
            body=body,
            query_params=query_params,
            path_params=path_params,
            content_type=content_type,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


