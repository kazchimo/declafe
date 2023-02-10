from typing import Any

import numpy as np
import polars as pl

from declafe.pl.feature_gen import ColLike
from declafe.pl.feature_gen.unary.unary_feature import UnaryFeature


class ConsecutiveCountFeature(UnaryFeature):

  def __init__(self, column: ColLike, target_value: Any):
    super().__init__(column)
    self.target_value = target_value

  def _unary_expr(self, orig_col: pl.Expr):

    def ap(s: pl.Series):
      arr = s.to_numpy()
      condition = (arr == self.target_value)
      gen_arr = np.frompyfunc(lambda b: np.arange(b), 1, 1)
      res = gen_arr(np.bincount(np.cumsum(condition != np.roll(condition, 1))))

      return pl.Series(condition * (np.concatenate(res) + 1))

    return orig_col.map(ap)

  def _feature_names(self) -> list[str]:
    return [
        "consecutive_count",
        str(self.target_value), "of", self._col_wrapped_feature_name
    ]
