import polars as pl
from pl.feature_gen.types import ColLike
import talib
from pl.feature_gen.unary.unary_feature import UnaryFeature


class SMAFeature(UnaryFeature):

  def __init__(self, column: ColLike, timeperiod: int):
    super().__init__(column)
    self.timeperiod = timeperiod

  def _unary_expr(self, orig_col: pl.Expr) -> pl.Expr:
    return orig_col.map(lambda s: talib.SMA(s, timeperiod=self.timeperiod))

  def _feature_names(self) -> list[str]:
    return [f'SMA({self.timeperiod})({self.column})']
