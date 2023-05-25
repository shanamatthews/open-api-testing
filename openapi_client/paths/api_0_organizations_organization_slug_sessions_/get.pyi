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

# Query params


class ProjectSchema(
    schemas.ListSchema
):


    class MetaOapg:
        items = schemas.IntSchema

    def __new__(
        cls,
        _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, decimal.Decimal, int, ]], typing.List[typing.Union[MetaOapg.items, decimal.Decimal, int, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'ProjectSchema':
        return super().__new__(
            cls,
            _arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)


class FieldSchema(
    schemas.ListSchema
):


    class MetaOapg:
        items = schemas.StrSchema

    def __new__(
        cls,
        _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'FieldSchema':
        return super().__new__(
            cls,
            _arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)


class EnvironmentSchema(
    schemas.ListSchema
):


    class MetaOapg:
        items = schemas.StrSchema

    def __new__(
        cls,
        _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'EnvironmentSchema':
        return super().__new__(
            cls,
            _arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)


class GroupBySchema(
    schemas.ListSchema
):


    class MetaOapg:
        items = schemas.StrSchema

    def __new__(
        cls,
        _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'GroupBySchema':
        return super().__new__(
            cls,
            _arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)
OrderBySchema = schemas.StrSchema
QuerySchema = schemas.StrSchema
StatsPeriodSchema = schemas.StrSchema
IntervalSchema = schemas.StrSchema
StatsPeriodStartSchema = schemas.StrSchema
StatsPeriodEndSchema = schemas.StrSchema
StartSchema = schemas.DateTimeSchema
EndSchema = schemas.DateTimeSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
        'project': typing.Union[ProjectSchema, list, tuple, ],
        'field': typing.Union[FieldSchema, list, tuple, ],
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'environment': typing.Union[EnvironmentSchema, list, tuple, ],
        'groupBy': typing.Union[GroupBySchema, list, tuple, ],
        'orderBy': typing.Union[OrderBySchema, str, ],
        'query': typing.Union[QuerySchema, str, ],
        'statsPeriod': typing.Union[StatsPeriodSchema, str, ],
        'interval': typing.Union[IntervalSchema, str, ],
        'statsPeriodStart': typing.Union[StatsPeriodStartSchema, str, ],
        'statsPeriodEnd': typing.Union[StatsPeriodEndSchema, str, ],
        'start': typing.Union[StartSchema, str, datetime, ],
        'end': typing.Union[EndSchema, str, datetime, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_project = api_client.QueryParameter(
    name="project",
    style=api_client.ParameterStyle.FORM,
    schema=ProjectSchema,
    required=True,
    explode=True,
)
request_query_field = api_client.QueryParameter(
    name="field",
    style=api_client.ParameterStyle.FORM,
    schema=FieldSchema,
    required=True,
    explode=True,
)
request_query_environment = api_client.QueryParameter(
    name="environment",
    style=api_client.ParameterStyle.FORM,
    schema=EnvironmentSchema,
    explode=True,
)
request_query_group_by = api_client.QueryParameter(
    name="groupBy",
    style=api_client.ParameterStyle.FORM,
    schema=GroupBySchema,
    explode=True,
)
request_query_order_by = api_client.QueryParameter(
    name="orderBy",
    style=api_client.ParameterStyle.FORM,
    schema=OrderBySchema,
    explode=True,
)
request_query_query = api_client.QueryParameter(
    name="query",
    style=api_client.ParameterStyle.FORM,
    schema=QuerySchema,
    explode=True,
)
request_query_stats_period = api_client.QueryParameter(
    name="statsPeriod",
    style=api_client.ParameterStyle.FORM,
    schema=StatsPeriodSchema,
    explode=True,
)
request_query_interval = api_client.QueryParameter(
    name="interval",
    style=api_client.ParameterStyle.FORM,
    schema=IntervalSchema,
    explode=True,
)
request_query_stats_period_start = api_client.QueryParameter(
    name="statsPeriodStart",
    style=api_client.ParameterStyle.FORM,
    schema=StatsPeriodStartSchema,
    explode=True,
)
request_query_stats_period_end = api_client.QueryParameter(
    name="statsPeriodEnd",
    style=api_client.ParameterStyle.FORM,
    schema=StatsPeriodEndSchema,
    explode=True,
)
request_query_start = api_client.QueryParameter(
    name="start",
    style=api_client.ParameterStyle.FORM,
    schema=StartSchema,
    explode=True,
)
request_query_end = api_client.QueryParameter(
    name="end",
    style=api_client.ParameterStyle.FORM,
    schema=EndSchema,
    explode=True,
)
# Path params
OrganizationSlugSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'organization_slug': typing.Union[OrganizationSlugSchema, str, ],
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


class SchemaFor200ResponseBodyApplicationJson(
    schemas.DictSchema
):


    class MetaOapg:
        required = {
            "intervals",
            "start",
            "groups",
            "end",
        }
        
        class properties:
            start = schemas.DateTimeSchema
            end = schemas.DateTimeSchema
            
            
            class intervals(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.DateTimeSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, datetime, ]], typing.List[typing.Union[MetaOapg.items, str, datetime, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'intervals':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class groups(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class items(
                        schemas.DictSchema
                    ):
                    
                    
                        class MetaOapg:
                            required = {
                                "series",
                                "by",
                                "totals",
                            }
                            
                            class properties:
                                by = schemas.DictSchema
                                totals = schemas.DictSchema
                                
                                
                                class series(
                                    schemas.DictSchema
                                ):
                                
                                
                                    class MetaOapg:
                                        
                                        
                                        class additional_properties(
                                            schemas.ListSchema
                                        ):
                                        
                                        
                                            class MetaOapg:
                                                items = schemas.IntSchema
                                        
                                            def __new__(
                                                cls,
                                                _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, decimal.Decimal, int, ]], typing.List[typing.Union[MetaOapg.items, decimal.Decimal, int, ]]],
                                                _configuration: typing.Optional[schemas.Configuration] = None,
                                            ) -> 'additional_properties':
                                                return super().__new__(
                                                    cls,
                                                    _arg,
                                                    _configuration=_configuration,
                                                )
                                        
                                            def __getitem__(self, i: int) -> MetaOapg.items:
                                                return super().__getitem__(i)
                                    
                                    def __getitem__(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                                        # dict_instance[name] accessor
                                        return super().__getitem__(name)
                                    
                                    def get_item_oapg(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                                        return super().get_item_oapg(name)
                                
                                    def __new__(
                                        cls,
                                        *_args: typing.Union[dict, frozendict.frozendict, ],
                                        _configuration: typing.Optional[schemas.Configuration] = None,
                                        **kwargs: typing.Union[MetaOapg.additional_properties, list, tuple, ],
                                    ) -> 'series':
                                        return super().__new__(
                                            cls,
                                            *_args,
                                            _configuration=_configuration,
                                            **kwargs,
                                        )
                                __annotations__ = {
                                    "by": by,
                                    "totals": totals,
                                    "series": series,
                                }
                        
                        series: MetaOapg.properties.series
                        by: MetaOapg.properties.by
                        totals: MetaOapg.properties.totals
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["by"]) -> MetaOapg.properties.by: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["totals"]) -> MetaOapg.properties.totals: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["series"]) -> MetaOapg.properties.series: ...
                        
                        @typing.overload
                        def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                        
                        def __getitem__(self, name: typing.Union[typing_extensions.Literal["by", "totals", "series", ], str]):
                            # dict_instance[name] accessor
                            return super().__getitem__(name)
                        
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["by"]) -> MetaOapg.properties.by: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["totals"]) -> MetaOapg.properties.totals: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["series"]) -> MetaOapg.properties.series: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                        
                        def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["by", "totals", "series", ], str]):
                            return super().get_item_oapg(name)
                        
                    
                        def __new__(
                            cls,
                            *_args: typing.Union[dict, frozendict.frozendict, ],
                            series: typing.Union[MetaOapg.properties.series, dict, frozendict.frozendict, ],
                            by: typing.Union[MetaOapg.properties.by, dict, frozendict.frozendict, ],
                            totals: typing.Union[MetaOapg.properties.totals, dict, frozendict.frozendict, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'items':
                            return super().__new__(
                                cls,
                                *_args,
                                series=series,
                                by=by,
                                totals=totals,
                                _configuration=_configuration,
                                **kwargs,
                            )
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'groups':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            __annotations__ = {
                "start": start,
                "end": end,
                "intervals": intervals,
                "groups": groups,
            }
    
    intervals: MetaOapg.properties.intervals
    start: MetaOapg.properties.start
    groups: MetaOapg.properties.groups
    end: MetaOapg.properties.end
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["start"]) -> MetaOapg.properties.start: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["end"]) -> MetaOapg.properties.end: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["intervals"]) -> MetaOapg.properties.intervals: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["groups"]) -> MetaOapg.properties.groups: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["start", "end", "intervals", "groups", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["start"]) -> MetaOapg.properties.start: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["end"]) -> MetaOapg.properties.end: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["intervals"]) -> MetaOapg.properties.intervals: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["groups"]) -> MetaOapg.properties.groups: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["start", "end", "intervals", "groups", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        intervals: typing.Union[MetaOapg.properties.intervals, list, tuple, ],
        start: typing.Union[MetaOapg.properties.start, str, datetime, ],
        groups: typing.Union[MetaOapg.properties.groups, list, tuple, ],
        end: typing.Union[MetaOapg.properties.end, str, datetime, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SchemaFor200ResponseBodyApplicationJson':
        return super().__new__(
            cls,
            *_args,
            intervals=intervals,
            start=start,
            groups=groups,
            end=end,
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


class SchemaFor400ResponseBodyApplicationJson(
    schemas.DictSchema
):


    class MetaOapg:
        required = {
            "detail",
        }
        
        class properties:
            detail = schemas.StrSchema
            __annotations__ = {
                "detail": detail,
            }
    
    detail: MetaOapg.properties.detail
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["detail"]) -> MetaOapg.properties.detail: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["detail", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["detail"]) -> MetaOapg.properties.detail: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["detail", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        detail: typing.Union[MetaOapg.properties.detail, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SchemaFor400ResponseBodyApplicationJson':
        return super().__new__(
            cls,
            *_args,
            detail=detail,
            _configuration=_configuration,
            **kwargs,
        )


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor400ResponseBodyApplicationJson,
    ]
    headers: schemas.Unset = schemas.unset


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationJson),
    },
)


@dataclass
class ApiResponseFor401(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: schemas.Unset = schemas.unset
    headers: schemas.Unset = schemas.unset


_response_for_401 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor401,
)


@dataclass
class ApiResponseFor403(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: schemas.Unset = schemas.unset
    headers: schemas.Unset = schemas.unset


_response_for_403 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor403,
)
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):
    @typing.overload
    def _retrieve_release_health_session_statistics_oapg(
        self,
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
    def _retrieve_release_health_session_statistics_oapg(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        query_params: RequestQueryParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def _retrieve_release_health_session_statistics_oapg(
        self,
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

    def _retrieve_release_health_session_statistics_oapg(
        self,
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
            request_query_project,
            request_query_field,
            request_query_environment,
            request_query_group_by,
            request_query_order_by,
            request_query_query,
            request_query_stats_period,
            request_query_interval,
            request_query_stats_period_start,
            request_query_stats_period_end,
            request_query_start,
            request_query_end,
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

        response = self.api_client.call_api(
            resource_path=used_path,
            method='get'.upper(),
            headers=_headers,
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


class RetrieveReleaseHealthSessionStatistics(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    @typing.overload
    def retrieve_release_health_session_statistics(
        self,
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
    def retrieve_release_health_session_statistics(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        query_params: RequestQueryParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def retrieve_release_health_session_statistics(
        self,
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

    def retrieve_release_health_session_statistics(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._retrieve_release_health_session_statistics_oapg(
            query_params=query_params,
            path_params=path_params,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    @typing.overload
    def get(
        self,
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
    def get(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        query_params: RequestQueryParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def get(
        self,
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

    def get(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._retrieve_release_health_session_statistics_oapg(
            query_params=query_params,
            path_params=path_params,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )

