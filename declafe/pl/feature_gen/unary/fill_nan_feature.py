from typing import Any

import polars as pl

from declafe.pl.feature_gen import FeatureGen
from declafe.pl.feature_gen.unary.unary_feature import UnaryFeature


class FillNanFeature(UnaryFeature):

  def __init__(self, column: "FeatureGen", fill_value: Any):
    super().__init__(column)
    self.fill_value = fill_value

  def _unary_expr(self, orig_col: pl.Expr):
    return orig_col.fill_nan(self.fill_value)

  def _feature_names(self) -> list[str]:
    return [f"fill_nan({self.col_feature.feature_name}, {self.fill_value})"]
