from abc import ABC, abstractmethod

import polars as pl

from pl.feature_gen.feature_gen import FeatureGen
from pl.feature_gen.types import ColLike


class UnaryFeature(FeatureGen, ABC):

  def __init__(self, column_name: ColLike):
    super().__init__()
    from pl.feature_gen import col_like_to_str
    self.column_name = col_like_to_str(column_name)

  def _expr(self) -> pl.Expr:
    return pl.col(self.column_name)

  @abstractmethod
  def _unary_expr(self, orig_col: pl.Expr):
    raise NotImplementedError
