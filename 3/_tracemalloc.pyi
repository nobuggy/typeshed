"""Stub file for the '_tracemalloc' module."""
# This is an autogenerated file. It serves as a starting point
# for a more precise manual annotation of this module.
# Feel free to edit the source below, but remove this header when you do.

from typing import List, Tuple, Dict, GenericType

def _get_object_traceback(*args, **kwargs) -> object: ...

def _get_traces() -> object:
    raise MemoryError()

def clear_traces() -> None: ...

def get_traceback_limit() -> long: ...

def get_traced_memory() -> tuple: ...

def get_tracemalloc_memory() -> object: ...

def is_tracing() -> bool: ...

def start(*args, **kwargs) -> None:
    raise ValueError()

def stop() -> None: ...