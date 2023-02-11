from typing import TYPE_CHECKING, Any, TypeVar, Callable, Iterable

from declafe.pl.feature_gen.feature_gen import FeatureGen
from declafe.pl.feature_gen.types import ColLike
from declafe.pl.feature_gen.constructor_dsl import *
from declafe.pl.feature_gen.talib_constructor import TalibConstructor

if TYPE_CHECKING:
  from declafe.pl.feature_gen.unary.id_feature import IdFeature
  from declafe.pl.feature_gen.const_feature import ConstFeature
  from declafe.pl.feature_gen.types import ColLike

talib = TalibConstructor()


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
  from declafe.pl.feature_gen.unary.id_feature import IdFeature
  return IdFeature(column_name)


def lit(value: Any) -> "ConstFeature":
  from declafe.pl.feature_gen.const_feature import ConstFeature
  return ConstFeature(value)


def conv_lit(value: Any) -> "FeatureGen":
  if isinstance(value, FeatureGen):
    return value
  else:
    return lit(value)


def const(value: Any) -> "ConstFeature":
  return lit(value)


def cond(test: Any, true: Any, false: Any) -> "FeatureGen":
  from declafe.pl.feature_gen.tri.cond_feature import CondFeature

  return CondFeature(conv_lit(test), conv_lit(true), conv_lit(false))


T = TypeVar("T")
Fun = Callable[[T], "FeatureGen"]
Ap = Callable[[Fun], "Features"]


def iter_over(it: Iterable[T]) -> Ap:

  def ap(f: Fun) -> "Features":
    return Features([f(x) for x in it])

  return ap
