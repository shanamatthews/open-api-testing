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


class SCIMMemberProvision(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "userName",
        }
        
        class properties:
            userName = schemas.StrSchema
            sentryOrgRole = schemas.StrSchema
            __annotations__ = {
                "userName": userName,
                "sentryOrgRole": sentryOrgRole,
            }
    
    userName: MetaOapg.properties.userName
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["userName"]) -> MetaOapg.properties.userName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sentryOrgRole"]) -> MetaOapg.properties.sentryOrgRole: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["userName", "sentryOrgRole", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["userName"]) -> MetaOapg.properties.userName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sentryOrgRole"]) -> typing.Union[MetaOapg.properties.sentryOrgRole, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["userName", "sentryOrgRole", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        userName: typing.Union[MetaOapg.properties.userName, str, ],
        sentryOrgRole: typing.Union[MetaOapg.properties.sentryOrgRole, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SCIMMemberProvision':
        return super().__new__(
            cls,
            *_args,
            userName=userName,
            sentryOrgRole=sentryOrgRole,
            _configuration=_configuration,
            **kwargs,
        )
