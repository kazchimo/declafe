from typing import Callable

import polars as pl

from declafe.pl.feature_gen.unary.unary_feature import UnaryFeature
from declafe.pl.feature_gen.types import ColLike


class FromFuncFeature(UnaryFeature):

  def __init__(self, column: ColLike, func: Callable[[pl.Series], pl.Series],
               op_name: str):
    super().__init__(column)
    self.func = func
    self.op_name = op_name

  def _unary_expr(self, orig_col: pl.Expr):
    return orig_col.map(self.func)

  def _feature_names(self) -> list[str]:
    return [f"{self.op_name}({self.col_feature.feature_name})"]
