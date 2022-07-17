from typing import Any, TYPE_CHECKING, List

from .ConstFeature import ConstFeature
from .Features import Features

if TYPE_CHECKING:
  from declafe.feature_gen.unary import IdFeature

__all__ = ["col", "c", "cols"]


def c(v: Any) -> ConstFeature:
  return ConstFeature(v)


def col(column_name: str) -> "IdFeature":
  from declafe.feature_gen.unary.IdFeature import IdFeature
  return IdFeature(column_name)


def cols(column_names: List[str]) -> "Features":
  return Features([col(co) for co in column_names])
