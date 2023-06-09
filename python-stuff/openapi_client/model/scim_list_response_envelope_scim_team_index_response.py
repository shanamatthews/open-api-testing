# coding: utf-8

"""
    API Reference

    Sentry Public API  # noqa: E501

    The version of the OpenAPI document: v0
    Contact: partners@sentry.io
    Generated by: https://openapi-generator.tech
"""

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


class SCIMListResponseEnvelopeSCIMTeamIndexResponse(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "startIndex",
            "totalResults",
            "itemsPerPage",
            "schemas",
            "Resources",
        }
        
        class properties:
            
            
            class schemas(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'schemas':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            totalResults = schemas.IntSchema
            startIndex = schemas.IntSchema
            itemsPerPage = schemas.IntSchema
            
            
            class Resources(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class items(
                        schemas.DictSchema
                    ):
                    
                    
                        class MetaOapg:
                            required = {
                                "displayName",
                                "meta",
                                "schemas",
                                "id",
                            }
                            
                            class properties:
                                
                                
                                class schemas(
                                    schemas.ListSchema
                                ):
                                
                                
                                    class MetaOapg:
                                        items = schemas.StrSchema
                                
                                    def __new__(
                                        cls,
                                        _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                                        _configuration: typing.Optional[schemas.Configuration] = None,
                                    ) -> 'schemas':
                                        return super().__new__(
                                            cls,
                                            _arg,
                                            _configuration=_configuration,
                                        )
                                
                                    def __getitem__(self, i: int) -> MetaOapg.items:
                                        return super().__getitem__(i)
                                id = schemas.StrSchema
                                displayName = schemas.StrSchema
                                
                                
                                class meta(
                                    schemas.DictSchema
                                ):
                                
                                
                                    class MetaOapg:
                                        required = {
                                            "resourceType",
                                        }
                                        
                                        class properties:
                                            resourceType = schemas.StrSchema
                                            __annotations__ = {
                                                "resourceType": resourceType,
                                            }
                                    
                                    resourceType: MetaOapg.properties.resourceType
                                    
                                    @typing.overload
                                    def __getitem__(self, name: typing_extensions.Literal["resourceType"]) -> MetaOapg.properties.resourceType: ...
                                    
                                    @typing.overload
                                    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                                    
                                    def __getitem__(self, name: typing.Union[typing_extensions.Literal["resourceType", ], str]):
                                        # dict_instance[name] accessor
                                        return super().__getitem__(name)
                                    
                                    
                                    @typing.overload
                                    def get_item_oapg(self, name: typing_extensions.Literal["resourceType"]) -> MetaOapg.properties.resourceType: ...
                                    
                                    @typing.overload
                                    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                                    
                                    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["resourceType", ], str]):
                                        return super().get_item_oapg(name)
                                    
                                
                                    def __new__(
                                        cls,
                                        *_args: typing.Union[dict, frozendict.frozendict, ],
                                        resourceType: typing.Union[MetaOapg.properties.resourceType, str, ],
                                        _configuration: typing.Optional[schemas.Configuration] = None,
                                        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                                    ) -> 'meta':
                                        return super().__new__(
                                            cls,
                                            *_args,
                                            resourceType=resourceType,
                                            _configuration=_configuration,
                                            **kwargs,
                                        )
                                
                                
                                class members(
                                    schemas.ListSchema
                                ):
                                
                                
                                    class MetaOapg:
                                        
                                        
                                        class items(
                                            schemas.DictSchema
                                        ):
                                        
                                        
                                            class MetaOapg:
                                                required = {
                                                    "display",
                                                    "value",
                                                }
                                                
                                                class properties:
                                                    value = schemas.StrSchema
                                                    display = schemas.StrSchema
                                                    __annotations__ = {
                                                        "value": value,
                                                        "display": display,
                                                    }
                                            
                                            display: MetaOapg.properties.display
                                            value: MetaOapg.properties.value
                                            
                                            @typing.overload
                                            def __getitem__(self, name: typing_extensions.Literal["value"]) -> MetaOapg.properties.value: ...
                                            
                                            @typing.overload
                                            def __getitem__(self, name: typing_extensions.Literal["display"]) -> MetaOapg.properties.display: ...
                                            
                                            @typing.overload
                                            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                                            
                                            def __getitem__(self, name: typing.Union[typing_extensions.Literal["value", "display", ], str]):
                                                # dict_instance[name] accessor
                                                return super().__getitem__(name)
                                            
                                            
                                            @typing.overload
                                            def get_item_oapg(self, name: typing_extensions.Literal["value"]) -> MetaOapg.properties.value: ...
                                            
                                            @typing.overload
                                            def get_item_oapg(self, name: typing_extensions.Literal["display"]) -> MetaOapg.properties.display: ...
                                            
                                            @typing.overload
                                            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                                            
                                            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["value", "display", ], str]):
                                                return super().get_item_oapg(name)
                                            
                                        
                                            def __new__(
                                                cls,
                                                *_args: typing.Union[dict, frozendict.frozendict, ],
                                                display: typing.Union[MetaOapg.properties.display, str, ],
                                                value: typing.Union[MetaOapg.properties.value, str, ],
                                                _configuration: typing.Optional[schemas.Configuration] = None,
                                                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                                            ) -> 'items':
                                                return super().__new__(
                                                    cls,
                                                    *_args,
                                                    display=display,
                                                    value=value,
                                                    _configuration=_configuration,
                                                    **kwargs,
                                                )
                                
                                    def __new__(
                                        cls,
                                        _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]]],
                                        _configuration: typing.Optional[schemas.Configuration] = None,
                                    ) -> 'members':
                                        return super().__new__(
                                            cls,
                                            _arg,
                                            _configuration=_configuration,
                                        )
                                
                                    def __getitem__(self, i: int) -> MetaOapg.items:
                                        return super().__getitem__(i)
                                __annotations__ = {
                                    "schemas": schemas,
                                    "id": id,
                                    "displayName": displayName,
                                    "meta": meta,
                                    "members": members,
                                }
                        
                        displayName: MetaOapg.properties.displayName
                        meta: MetaOapg.properties.meta
                        schemas: MetaOapg.properties.schemas
                        id: MetaOapg.properties.id
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["schemas"]) -> MetaOapg.properties.schemas: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["displayName"]) -> MetaOapg.properties.displayName: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["meta"]) -> MetaOapg.properties.meta: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["members"]) -> MetaOapg.properties.members: ...
                        
                        @typing.overload
                        def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                        
                        def __getitem__(self, name: typing.Union[typing_extensions.Literal["schemas", "id", "displayName", "meta", "members", ], str]):
                            # dict_instance[name] accessor
                            return super().__getitem__(name)
                        
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["schemas"]) -> MetaOapg.properties.schemas: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["displayName"]) -> MetaOapg.properties.displayName: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["meta"]) -> MetaOapg.properties.meta: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["members"]) -> typing.Union[MetaOapg.properties.members, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                        
                        def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["schemas", "id", "displayName", "meta", "members", ], str]):
                            return super().get_item_oapg(name)
                        
                    
                        def __new__(
                            cls,
                            *_args: typing.Union[dict, frozendict.frozendict, ],
                            displayName: typing.Union[MetaOapg.properties.displayName, str, ],
                            meta: typing.Union[MetaOapg.properties.meta, dict, frozendict.frozendict, ],
                            schemas: typing.Union[MetaOapg.properties.schemas, list, tuple, ],
                            id: typing.Union[MetaOapg.properties.id, str, ],
                            members: typing.Union[MetaOapg.properties.members, list, tuple, schemas.Unset] = schemas.unset,
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'items':
                            return super().__new__(
                                cls,
                                *_args,
                                displayName=displayName,
                                meta=meta,
                                schemas=schemas,
                                id=id,
                                members=members,
                                _configuration=_configuration,
                                **kwargs,
                            )
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'Resources':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            __annotations__ = {
                "schemas": schemas,
                "totalResults": totalResults,
                "startIndex": startIndex,
                "itemsPerPage": itemsPerPage,
                "Resources": Resources,
            }
    
    startIndex: MetaOapg.properties.startIndex
    totalResults: MetaOapg.properties.totalResults
    itemsPerPage: MetaOapg.properties.itemsPerPage
    schemas: MetaOapg.properties.schemas
    Resources: MetaOapg.properties.Resources
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["schemas"]) -> MetaOapg.properties.schemas: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["totalResults"]) -> MetaOapg.properties.totalResults: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["startIndex"]) -> MetaOapg.properties.startIndex: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["itemsPerPage"]) -> MetaOapg.properties.itemsPerPage: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Resources"]) -> MetaOapg.properties.Resources: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["schemas", "totalResults", "startIndex", "itemsPerPage", "Resources", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["schemas"]) -> MetaOapg.properties.schemas: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["totalResults"]) -> MetaOapg.properties.totalResults: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["startIndex"]) -> MetaOapg.properties.startIndex: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["itemsPerPage"]) -> MetaOapg.properties.itemsPerPage: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Resources"]) -> MetaOapg.properties.Resources: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["schemas", "totalResults", "startIndex", "itemsPerPage", "Resources", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        startIndex: typing.Union[MetaOapg.properties.startIndex, decimal.Decimal, int, ],
        totalResults: typing.Union[MetaOapg.properties.totalResults, decimal.Decimal, int, ],
        itemsPerPage: typing.Union[MetaOapg.properties.itemsPerPage, decimal.Decimal, int, ],
        schemas: typing.Union[MetaOapg.properties.schemas, list, tuple, ],
        Resources: typing.Union[MetaOapg.properties.Resources, list, tuple, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SCIMListResponseEnvelopeSCIMTeamIndexResponse':
        return super().__new__(
            cls,
            *_args,
            startIndex=startIndex,
            totalResults=totalResults,
            itemsPerPage=itemsPerPage,
            schemas=schemas,
            Resources=Resources,
            _configuration=_configuration,
            **kwargs,
        )
