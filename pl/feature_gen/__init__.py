from typing import TYPE_CHECKING, Any

from pl.feature_gen.feature_gen import FeatureGen
from pl.feature_gen.types import ColLike
from pl.feature_gen.unary.id_feature import IdFeature

if TYPE_CHECKING:
  from pl.feature_gen.unary.id_feature import IdFeature
  from pl.feature_gen.const_feature import ConstFeature
  from pl.feature_gen.types import ColLike


def col_like_to_str(col_like: ColLike) -> str:
  if isinstance(col_like, str):
    return col_like
  elif isinstance(col_like, FeatureGen):
    return col_like.feature_name
  else:
    raise TypeError(f"Expected str or FeatureGen, got {type(col_like)}")


def col_like_to_feature_gen(col_like: ColLike) -> "FeatureGen":
  if isinstance(col_like, str):
    return col(col_like)
  elif isinstance(col_like, FeatureGen):
    return col_like
  else:
    raise TypeError(f"Expected str or FeatureGen, got {type(col_like)}")


def col(column_name: str) -> "IdFeature":
  from pl.feature_gen.unary.id_feature import IdFeature
  return IdFeature(column_name)


def lit(value: Any) -> "ConstFeature":
  from pl.feature_gen.const_feature import ConstFeature
  return ConstFeature(value)


def const(value: Any) -> "ConstFeature":
  return lit(value)
