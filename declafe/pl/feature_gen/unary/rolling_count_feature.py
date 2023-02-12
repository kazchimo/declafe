from typing import Any

import polars as pl

from declafe.pl.feature_gen import FeatureGen
from declafe.pl.feature_gen.unary.unary_feature import UnaryFeature


class RollingCountFeature(UnaryFeature):

  def __init__(self, column: FeatureGen, window: int, target_value: Any):
    super().__init__(column)
    self.window = window
    self.target_value = target_value

  def _unary_expr(self, orig_col: pl.Expr) -> pl.Expr:
    return pl.when(
        orig_col == self.target_value).then(1).otherwise(0).rolling_sum(
            self.window)

  def _feature_names(self) -> list[str]:
    return [
        "rolling_count",
        str(self.target_value), "over", self.col_feature.wrapped_feature_name,
        str(self.window)
    ]
