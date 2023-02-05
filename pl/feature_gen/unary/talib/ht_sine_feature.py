import polars as pl
from pl.feature_gen.types import ColLike
import talib
from pl.feature_gen.unary.unary_feature import UnaryFeature


class HT_SINE_0Feature(UnaryFeature):

  def __init__(self, column: ColLike):
    super().__init__(column)

  def _unary_expr(self, orig_col: pl.Expr) -> pl.Expr:
    return orig_col.map(lambda s: talib.HT_SINE(s,)[0])

  def _feature_names(self) -> list[str]:
    return [f'HT_SINE_0()({self.column})']


class HT_SINE_1Feature(UnaryFeature):

  def __init__(self, column: ColLike):
    super().__init__(column)

  def _unary_expr(self, orig_col: pl.Expr) -> pl.Expr:
    return orig_col.map(lambda s: talib.HT_SINE(s,)[1])

  def _feature_names(self) -> list[str]:
    return [f'HT_SINE_1()({self.column})']
