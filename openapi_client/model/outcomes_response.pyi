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


class OutcomesResponse(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "intervals",
            "start",
            "groups",
            "end",
        }
        
        class properties:
            start = schemas.StrSchema
            end = schemas.StrSchema
            
            
            class intervals(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
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
                                
                                
                                class by(
                                    schemas.DictSchema
                                ):
                                
                                
                                    class MetaOapg:
                                        additional_properties = schemas.AnyTypeSchema
                                    
                                    def __getitem__(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                                        # dict_instance[name] accessor
                                        return super().__getitem__(name)
                                    
                                    def get_item_oapg(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                                        return super().get_item_oapg(name)
                                
                                    def __new__(
                                        cls,
                                        *_args: typing.Union[dict, frozendict.frozendict, ],
                                        _configuration: typing.Optional[schemas.Configuration] = None,
                                        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                                    ) -> 'by':
                                        return super().__new__(
                                            cls,
                                            *_args,
                                            _configuration=_configuration,
                                            **kwargs,
                                        )
                                
                                
                                class totals(
                                    schemas.DictSchema
                                ):
                                
                                
                                    class MetaOapg:
                                        additional_properties = schemas.AnyTypeSchema
                                    
                                    def __getitem__(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                                        # dict_instance[name] accessor
                                        return super().__getitem__(name)
                                    
                                    def get_item_oapg(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                                        return super().get_item_oapg(name)
                                
                                    def __new__(
                                        cls,
                                        *_args: typing.Union[dict, frozendict.frozendict, ],
                                        _configuration: typing.Optional[schemas.Configuration] = None,
                                        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                                    ) -> 'totals':
                                        return super().__new__(
                                            cls,
                                            *_args,
                                            _configuration=_configuration,
                                            **kwargs,
                                        )
                                
                                
                                class series(
                                    schemas.DictSchema
                                ):
                                
                                
                                    class MetaOapg:
                                        additional_properties = schemas.AnyTypeSchema
                                    
                                    def __getitem__(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                                        # dict_instance[name] accessor
                                        return super().__getitem__(name)
                                    
                                    def get_item_oapg(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                                        return super().get_item_oapg(name)
                                
                                    def __new__(
                                        cls,
                                        *_args: typing.Union[dict, frozendict.frozendict, ],
                                        _configuration: typing.Optional[schemas.Configuration] = None,
                                        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
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
        start: typing.Union[MetaOapg.properties.start, str, ],
        groups: typing.Union[MetaOapg.properties.groups, list, tuple, ],
        end: typing.Union[MetaOapg.properties.end, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OutcomesResponse':
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
