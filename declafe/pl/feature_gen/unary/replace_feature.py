from typing import TypeVar

import polars as pl

from declafe.pl.feature_gen.unary.unary_feature import UnaryFeature
from declafe.pl.feature_gen.types import ColLike

T = TypeVar("T")


class ReplaceFeature(UnaryFeature):

  def __init__(self, column: ColLike, target_value: T, to_value: T):
    super().__init__(column)
    self.target_value = target_value
    self.to_value = to_value

  def _unary_expr(self, orig_col: pl.Expr):
    return pl\
      .when(orig_col.eq(self.target_value))\
      .then(pl.lit(self.to_value))\
      .otherwise(orig_col)

  def _feature_names(self) -> list[str]:
    return [
        "replace",
        str(self.target_value),
        "of",
        self._col_wrapped_feature_name,
        "to",
        str(self.to_value),
    ]
