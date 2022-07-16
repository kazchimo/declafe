from typing import Any, TYPE_CHECKING, List

from . import Features
from .ConstFeature import ConstFeature

if TYPE_CHECKING:
  from .unary import IdFeature
  
__all__ = ["col", "c", "cols"]


def c(v: Any) -> ConstFeature:
  return ConstFeature(v)


def col(column_name: str) -> "IdFeature":
  from .unary.IdFeature import IdFeature
  return IdFeature(column_name)

def cols(column_names: List[str]) -> "Features":
  return Features([col(co) for co in column_names])
