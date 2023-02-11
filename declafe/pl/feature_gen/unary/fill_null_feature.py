from typing import Any, Optional

import polars as pl
from polars.internals.type_aliases import FillNullStrategy

from declafe.pl.feature_gen import FeatureGen
from declafe.pl.feature_gen.unary.unary_feature import UnaryFeature


class FillNullFeature(UnaryFeature):

  def __init__(self, column: "FeatureGen", fill_value: Optional[Any],
               strategy: Optional[FillNullStrategy], limit: Optional[int]):
    super().__init__(column)
    self.fill_value = fill_value
    self.strategy = strategy
    self.limit = limit

  def _unary_expr(self, orig_col: pl.Expr):
    return orig_col.fill_null(self.fill_value, self.strategy, self.limit)

  def _feature_names(self) -> list[str]:
    if self.fill_value is not None:
      return [f"fill_null({self.col_feature.feature_name}, {self.fill_value})"]
    elif self.strategy is not None:
      return [f"{self.strategy}_fill_null({self.col_feature.feature_name})"]
    else:
      raise ValueError("Either fill_value or strategy must be specified")
