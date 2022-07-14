from typing import Any, TYPE_CHECKING

from .ConstFeature import ConstFeature

if TYPE_CHECKING:
  from .unary import IdFeature


def c(v: Any) -> ConstFeature:
  return ConstFeature(v)


def col(column_name: str) -> "IdFeature":
  from .unary.IdFeature import IdFeature
  return IdFeature(column_name)
