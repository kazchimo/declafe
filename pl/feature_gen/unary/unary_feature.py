from abc import ABC, abstractmethod

import polars as pl

from pl.feature_gen.feature_gen import FeatureGen
from pl.feature_gen.types import ColLike


class UnaryFeature(FeatureGen, ABC):

  def __init__(self, column: ColLike):
    super().__init__()
    self.column = column

  def _expr(self) -> pl.Expr:
    from pl.feature_gen.unary.id_feature import IdFeature

    if isinstance(self, IdFeature):
      return self._unary_expr(pl.lit(0))
    else:
      return self._unary_expr(self.col_feature.expr())

  @abstractmethod
  def _unary_expr(self, orig_col: pl.Expr):
    raise NotImplementedError

  @property
  def _wrapped_column_name(self) -> str:
    from pl.feature_gen.const_feature import ConstFeature
    from pl.feature_gen.unary.id_feature import IdFeature

    if isinstance(self.column, str):
      return self.column
    elif isinstance(self.column, (IdFeature, ConstFeature)):
      return self.column.feature_name
    else:
      return f"({self.column.feature_name})"

  @property
  def col_feature(self):
    from pl.feature_gen import col_like_to_feature_gen
    return col_like_to_feature_gen(self.column)
