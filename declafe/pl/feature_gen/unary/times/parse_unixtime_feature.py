from typing import Literal
from declafe.pl.feature_gen.types import ColLike

import polars as pl

from ..unary_feature import UnaryFeature

Unit = Literal["ns", "us", "ms", "s", "d"]


class ParseUnixTimeFeature(UnaryFeature):

  def __init__(self, column: ColLike, unit: Unit):
    super().__init__(column)
    self.unit: Unit = unit

  def _unary_expr(self, orig_col: pl.Expr):
    return pl.from_epoch(orig_col, self.unit)

  def _feature_names(self) -> list[str]:
    return [f"parse_unixtime({self.col_feature.feature_name})"]
