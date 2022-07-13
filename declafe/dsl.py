from typing import Any, TYPE_CHECKING

from declafe.ConstFeature import ConstFeature

if TYPE_CHECKING:
  from declafe.unary.IdFeature import IdFeature

def c(v: Any) -> ConstFeature:
  return ConstFeature(v)

def col(column_name: str) -> "IdFeature":
  from declafe.unary.IdFeature import IdFeature
  return IdFeature(column_name)
