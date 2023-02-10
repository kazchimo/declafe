from typing import Any, Callable

import polars as pl
import numpy as np

from declafe.pl.feature_gen.unary.unary_feature import UnaryFeature
from declafe.pl.feature_gen.types import ColLike


class AccumulateFeature(UnaryFeature):

  def __init__(self, column: ColLike, ops_name: str,
               ops_func: Callable[[Any, Any], Any]):
    super().__init__(column)
    self.ops_name = ops_name
    self.ops_func = ops_func

  def _unary_expr(self, orig_col: pl.Expr):

    def ap(s: pl.Series) -> pl.Series:
      arr = np.frompyfunc(self.ops_func, 2, 1).accumulate(s.to_numpy())
      return pl.Series(arr.tolist(), dtype=pl.Float64)

    return orig_col.map(ap)

  def _feature_names(self) -> list[str]:
    return [f"accumulate_{self.ops_name}({self.col_feature.feature_name})"]
