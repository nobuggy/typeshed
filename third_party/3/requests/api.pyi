# Stubs for requests.api (Python 3)

from typing import Optional, Union, Any, Iterable, Mapping, MutableMapping, Tuple, IO, Text

from .models import Response

_ParamsMappingValueType = Union[str, bytes, int, float, Iterable[Union[str, bytes, int, float]]]
_Data = Union[None, bytes, MutableMapping[Text, Text], IO]

def request(method: str, url: str, **kwargs) -> Response: ...
def get(url: Union[str, bytes],
        params: Optional[
            Union[
                Mapping[Union[str, bytes, int, float], _ParamsMappingValueType],
                Union[str, bytes],
                Tuple[Union[str, bytes, int, float], _ParamsMappingValueType],
                Mapping[str, _ParamsMappingValueType],
                Mapping[bytes, _ParamsMappingValueType],
                Mapping[int, _ParamsMappingValueType],
                Mapping[float, _ParamsMappingValueType]]]=None,
        **kwargs) -> Response: ...
def options(url: str, **kwargs) -> Response: ...
def head(url: str, **kwargs) -> Response: ...
def post(url: str, data: _Data = ..., json: Optional[MutableMapping] = ..., **kwargs) -> Response: ...
def put(url: str, data: _Data = ..., **kwargs) -> Response: ...
def patch(url: str, data: _Data = ..., **kwargs) -> Response: ...
def delete(url: str, **kwargs) -> Response: ...
