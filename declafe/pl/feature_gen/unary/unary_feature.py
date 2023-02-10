from abc import ABC, abstractmethod

import polars as pl

from declafe.pl.feature_gen.feature_gen import FeatureGen
from declafe.pl.feature_gen.types import ColLike


class UnaryFeature(FeatureGen, ABC):

  def __init__(self, column: ColLike):
    super().__init__()
    self.column = column

  def _expr(self) -> pl.Expr:
    from declafe.pl.feature_gen.unary.id_feature import IdFeature

    if isinstance(self, IdFeature):
      return self._unary_expr(pl.lit(0))  # type: ignore
    else:
      return self._unary_expr(self.col_feature.expr())

  @abstractmethod
  def _unary_expr(self, orig_col: pl.Expr) -> pl.Expr:
    raise NotImplementedError

  @property
  def col_feature(self) -> "FeatureGen":
    from declafe.pl.feature_gen import col_like_to_feature_gen
    return col_like_to_feature_gen(self.column)

  @property
  def _col_wrapped_feature_name(self) -> str:
    return self.col_feature.wrapped_feature_name
