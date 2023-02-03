from abc import ABC, abstractmethod

import polars as pl

from pl.feature_gen.feature_gen import FeatureGen
from pl.feature_gen.types import ColLike


class UnaryFeature(FeatureGen, ABC):

  def __init__(self, column_name: ColLike):
    super().__init__()
    self.column_name = column_name

  def _expr(self) -> pl.Expr:
    return pl.col(self.col_feature.feature_name)

  @abstractmethod
  def _unary_expr(self, orig_col: pl.Expr):
    raise NotImplementedError

  @property
  def col_feature(self):
    from pl.feature_gen import col_like_to_feature_gen
    return col_like_to_feature_gen(self.column_name)
