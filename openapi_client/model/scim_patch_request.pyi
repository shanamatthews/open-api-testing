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


class SCIMPatchRequest(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "Operations",
        }
        
        class properties:
            
            
            class Operations(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class items(
                        schemas.DictSchema
                    ):
                    
                    
                        class MetaOapg:
                            required = {
                                "op",
                                "value",
                            }
                            
                            class properties:
                                op = schemas.StrSchema
                                value = schemas.AnyTypeSchema
                                path = schemas.StrSchema
                                __annotations__ = {
                                    "op": op,
                                    "value": value,
                                    "path": path,
                                }
                        
                        op: MetaOapg.properties.op
                        value: MetaOapg.properties.value
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["op"]) -> MetaOapg.properties.op: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["value"]) -> MetaOapg.properties.value: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["path"]) -> MetaOapg.properties.path: ...
                        
                        @typing.overload
                        def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                        
                        def __getitem__(self, name: typing.Union[typing_extensions.Literal["op", "value", "path", ], str]):
                            # dict_instance[name] accessor
                            return super().__getitem__(name)
                        
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["op"]) -> MetaOapg.properties.op: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["value"]) -> MetaOapg.properties.value: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["path"]) -> typing.Union[MetaOapg.properties.path, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                        
                        def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["op", "value", "path", ], str]):
                            return super().get_item_oapg(name)
                        
                    
                        def __new__(
                            cls,
                            *_args: typing.Union[dict, frozendict.frozendict, ],
                            op: typing.Union[MetaOapg.properties.op, str, ],
                            value: typing.Union[MetaOapg.properties.value, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                            path: typing.Union[MetaOapg.properties.path, str, schemas.Unset] = schemas.unset,
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'items':
                            return super().__new__(
                                cls,
                                *_args,
                                op=op,
                                value=value,
                                path=path,
                                _configuration=_configuration,
                                **kwargs,
                            )
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'Operations':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
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
            __annotations__ = {
                "Operations": Operations,
                "schemas": schemas,
            }
    
    Operations: MetaOapg.properties.Operations
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Operations"]) -> MetaOapg.properties.Operations: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["schemas"]) -> MetaOapg.properties.schemas: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["Operations", "schemas", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Operations"]) -> MetaOapg.properties.Operations: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["schemas"]) -> typing.Union[MetaOapg.properties.schemas, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["Operations", "schemas", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        Operations: typing.Union[MetaOapg.properties.Operations, list, tuple, ],
        schemas: typing.Union[MetaOapg.properties.schemas, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SCIMPatchRequest':
        return super().__new__(
            cls,
            *_args,
            Operations=Operations,
            schemas=schemas,
            _configuration=_configuration,
            **kwargs,
        )
