"""
This module contains types that are outward-facing, to be imported and used by users of the package.
"""
from typing import Literal, TypeAlias

from .backend import BackendArgument


ReturnKey: TypeAlias = Literal['none', 'idx', 'input']
Error: TypeAlias = Literal['raise', 'ignore', 'log', 'return']
