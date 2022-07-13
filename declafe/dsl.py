from typing import Any, TYPE_CHECKING

from lib.features.ConstFeature import ConstFeature

if TYPE_CHECKING:
  from lib.features.unary.IdFeature import IdFeature

def c(v: Any) -> ConstFeature:
  return ConstFeature(v)

def col(column_name: str) -> "IdFeature":
  from lib.features.unary.IdFeature import IdFeature
  return IdFeature(column_name)
