from typing import Any

import polars as pl

from declafe.pl.feature_gen.unary.unary_feature import UnaryFeature
from declafe.pl.feature_gen.types import ColLike
import numpy as np


class ExistsWithinFeature(UnaryFeature):

  def __init__(self, column: ColLike, target_value: Any, period: int):
    super().__init__(column)
    self.period = period
    self.target_value = target_value

  def _unary_expr(self, orig_col: pl.Expr):

    def ap(s: pl.Series) -> pl.Series:
      arr = s.to_numpy()
      tv = self.target_value
      p = self.period

      def check(idx: int) -> bool:
        return tv in arr[idx - p + 1:idx + 1]

      return pl.Series(np.frompyfunc(check, 1, 1)(np.arange(len(arr))).tolist())

    return orig_col.map(ap).cast(pl.Boolean)

  def _feature_names(self) -> list[str]:
    return [
        f"{self.target_value}",
        "of",
        f"{self.col_feature.wrapped_feature_name}",
        f"exists_within{self.period}",
    ]
