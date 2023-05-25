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


class MonitorAlertRuleTargetValidator(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "target_identifier",
            "target_type",
        }
        
        class properties:
            target_identifier = schemas.IntSchema
            target_type = schemas.StrSchema
            __annotations__ = {
                "target_identifier": target_identifier,
                "target_type": target_type,
            }
    
    target_identifier: MetaOapg.properties.target_identifier
    target_type: MetaOapg.properties.target_type
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["target_identifier"]) -> MetaOapg.properties.target_identifier: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["target_type"]) -> MetaOapg.properties.target_type: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["target_identifier", "target_type", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["target_identifier"]) -> MetaOapg.properties.target_identifier: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["target_type"]) -> MetaOapg.properties.target_type: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["target_identifier", "target_type", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        target_identifier: typing.Union[MetaOapg.properties.target_identifier, decimal.Decimal, int, ],
        target_type: typing.Union[MetaOapg.properties.target_type, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'MonitorAlertRuleTargetValidator':
        return super().__new__(
            cls,
            *_args,
            target_identifier=target_identifier,
            target_type=target_type,
            _configuration=_configuration,
            **kwargs,
        )