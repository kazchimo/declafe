import polars as pl
from pl.feature_gen.types import ColLike
import talib

from pl.feature_gen.unary.unary_feature import UnaryFeature


class T3Feature(UnaryFeature):

  def __init__(self, column: ColLike, timeperiod: int, vfactor: float):
    super().__init__(column)
    self.timeperiod = timeperiod
    self.vfactor = vfactor

  def _unary_expr(self, orig_col: pl.Expr) -> pl.Expr:
    return orig_col.map(
        lambda s: talib.T3(s, timeperiod=self.timeperiod, vfactor=self.vfactor))

  def _feature_names(self) -> list[str]:
    return [f'T3({self.timeperiod}, {self.vfactor})({self.column})']
