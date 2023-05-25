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
OwnerSchema = schemas.BoolSchema
CursorSchema = schemas.StrSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'owner': typing.Union[OwnerSchema, bool, ],
        'cursor': typing.Union[CursorSchema, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_owner = api_client.QueryParameter(
    name="owner",
    style=api_client.ParameterStyle.FORM,
    schema=OwnerSchema,
    explode=True,
)
request_query_cursor = api_client.QueryParameter(
    name="cursor",
    style=api_client.ParameterStyle.FORM,
    schema=CursorSchema,
    explode=True,
)


class SchemaFor200ResponseBodyApplicationJson(
    schemas.ListSchema
):


    class MetaOapg:
        
        
        class items(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                required = {
                    "dateCreated",
                    "name",
                    "avatar",
                    "id",
                    "isEarlyAdopter",
                    "require2FA",
                    "slug",
                    "status",
                }
                
                class properties:
                    
                    
                    class avatar(
                        schemas.DictSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            class properties:
                                avatarType = schemas.StrSchema
                                
                                
                                class avatarUuid(
                                    schemas.StrBase,
                                    schemas.NoneBase,
                                    schemas.Schema,
                                    schemas.NoneStrMixin
                                ):
                                
                                
                                    def __new__(
                                        cls,
                                        *_args: typing.Union[None, str, ],
                                        _configuration: typing.Optional[schemas.Configuration] = None,
                                    ) -> 'avatarUuid':
                                        return super().__new__(
                                            cls,
                                            *_args,
                                            _configuration=_configuration,
                                        )
                                __annotations__ = {
                                    "avatarType": avatarType,
                                    "avatarUuid": avatarUuid,
                                }
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["avatarType"]) -> MetaOapg.properties.avatarType: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["avatarUuid"]) -> MetaOapg.properties.avatarUuid: ...
                        
                        @typing.overload
                        def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                        
                        def __getitem__(self, name: typing.Union[typing_extensions.Literal["avatarType", "avatarUuid", ], str]):
                            # dict_instance[name] accessor
                            return super().__getitem__(name)
                        
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["avatarType"]) -> typing.Union[MetaOapg.properties.avatarType, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["avatarUuid"]) -> typing.Union[MetaOapg.properties.avatarUuid, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                        
                        def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["avatarType", "avatarUuid", ], str]):
                            return super().get_item_oapg(name)
                        
                    
                        def __new__(
                            cls,
                            *_args: typing.Union[dict, frozendict.frozendict, ],
                            avatarType: typing.Union[MetaOapg.properties.avatarType, str, schemas.Unset] = schemas.unset,
                            avatarUuid: typing.Union[MetaOapg.properties.avatarUuid, None, str, schemas.Unset] = schemas.unset,
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'avatar':
                            return super().__new__(
                                cls,
                                *_args,
                                avatarType=avatarType,
                                avatarUuid=avatarUuid,
                                _configuration=_configuration,
                                **kwargs,
                            )
                    dateCreated = schemas.DateTimeSchema
                    id = schemas.StrSchema
                    isEarlyAdopter = schemas.BoolSchema
                    name = schemas.StrSchema
                    require2FA = schemas.BoolSchema
                    slug = schemas.StrSchema
                    
                    
                    class status(
                        schemas.DictSchema
                    ):
                    
                    
                        class MetaOapg:
                            required = {
                                "name",
                                "id",
                            }
                            
                            class properties:
                                id = schemas.StrSchema
                                name = schemas.StrSchema
                                __annotations__ = {
                                    "id": id,
                                    "name": name,
                                }
                        
                        name: MetaOapg.properties.name
                        id: MetaOapg.properties.id
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
                        
                        @typing.overload
                        def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                        
                        def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "name", ], str]):
                            # dict_instance[name] accessor
                            return super().__getitem__(name)
                        
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                        
                        def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "name", ], str]):
                            return super().get_item_oapg(name)
                        
                    
                        def __new__(
                            cls,
                            *_args: typing.Union[dict, frozendict.frozendict, ],
                            name: typing.Union[MetaOapg.properties.name, str, ],
                            id: typing.Union[MetaOapg.properties.id, str, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'status':
                            return super().__new__(
                                cls,
                                *_args,
                                name=name,
                                id=id,
                                _configuration=_configuration,
                                **kwargs,
                            )
                    __annotations__ = {
                        "avatar": avatar,
                        "dateCreated": dateCreated,
                        "id": id,
                        "isEarlyAdopter": isEarlyAdopter,
                        "name": name,
                        "require2FA": require2FA,
                        "slug": slug,
                        "status": status,
                    }
            
            dateCreated: MetaOapg.properties.dateCreated
            name: MetaOapg.properties.name
            avatar: MetaOapg.properties.avatar
            id: MetaOapg.properties.id
            isEarlyAdopter: MetaOapg.properties.isEarlyAdopter
            require2FA: MetaOapg.properties.require2FA
            slug: MetaOapg.properties.slug
            status: MetaOapg.properties.status
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["avatar"]) -> MetaOapg.properties.avatar: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["dateCreated"]) -> MetaOapg.properties.dateCreated: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["isEarlyAdopter"]) -> MetaOapg.properties.isEarlyAdopter: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["require2FA"]) -> MetaOapg.properties.require2FA: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["slug"]) -> MetaOapg.properties.slug: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["avatar", "dateCreated", "id", "isEarlyAdopter", "name", "require2FA", "slug", "status", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["avatar"]) -> MetaOapg.properties.avatar: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["dateCreated"]) -> MetaOapg.properties.dateCreated: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["isEarlyAdopter"]) -> MetaOapg.properties.isEarlyAdopter: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["require2FA"]) -> MetaOapg.properties.require2FA: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["slug"]) -> MetaOapg.properties.slug: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["avatar", "dateCreated", "id", "isEarlyAdopter", "name", "require2FA", "slug", "status", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *_args: typing.Union[dict, frozendict.frozendict, ],
                dateCreated: typing.Union[MetaOapg.properties.dateCreated, str, datetime, ],
                name: typing.Union[MetaOapg.properties.name, str, ],
                avatar: typing.Union[MetaOapg.properties.avatar, dict, frozendict.frozendict, ],
                id: typing.Union[MetaOapg.properties.id, str, ],
                isEarlyAdopter: typing.Union[MetaOapg.properties.isEarlyAdopter, bool, ],
                require2FA: typing.Union[MetaOapg.properties.require2FA, bool, ],
                slug: typing.Union[MetaOapg.properties.slug, str, ],
                status: typing.Union[MetaOapg.properties.status, dict, frozendict.frozendict, ],
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'items':
                return super().__new__(
                    cls,
                    *_args,
                    dateCreated=dateCreated,
                    name=name,
                    avatar=avatar,
                    id=id,
                    isEarlyAdopter=isEarlyAdopter,
                    require2FA=require2FA,
                    slug=slug,
                    status=status,
                    _configuration=_configuration,
                    **kwargs,
                )

    def __new__(
        cls,
        _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'SchemaFor200ResponseBodyApplicationJson':
        return super().__new__(
            cls,
            _arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)


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
    def _list_your_organizations_oapg(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def _list_your_organizations_oapg(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def _list_your_organizations_oapg(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def _list_your_organizations_oapg(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
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
        used_path = path.value

        prefix_separator_iterator = None
        for parameter in (
            request_query_owner,
            request_query_cursor,
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


class ListYourOrganizations(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    @typing.overload
    def list_your_organizations(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def list_your_organizations(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def list_your_organizations(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def list_your_organizations(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._list_your_organizations_oapg(
            query_params=query_params,
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
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def get(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
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
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._list_your_organizations_oapg(
            query_params=query_params,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


