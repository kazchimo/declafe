import polars as pl
from pl.feature_gen.types import ColLike
import talib

from pl.feature_gen.unary.unary_feature import UnaryFeature


class STDDEVFeature(UnaryFeature):

  def __init__(self, column: ColLike, timeperiod: int, nbdev: float):
    super().__init__(column)
    self.timeperiod = timeperiod
    self.nbdev = nbdev

  def _unary_expr(self, orig_col: pl.Expr) -> pl.Expr:
    return orig_col.map(
        lambda s: talib.STDDEV(s, timeperiod=self.timeperiod, nbdev=self.nbdev))

  def _feature_names(self) -> list[str]:
    return [f'STDDEV({self.timeperiod}, {self.nbdev})({self.column})']
