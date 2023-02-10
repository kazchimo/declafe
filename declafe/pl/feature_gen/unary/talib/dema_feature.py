import polars as pl
from declafe.pl.feature_gen.types import ColLike
import talib

from declafe.pl.feature_gen.unary.unary_feature import UnaryFeature


class DEMAFeature(UnaryFeature):

  def __init__(self, close: ColLike, timeperiod: int):
    super().__init__(close)
    self.timeperiod = timeperiod

  def _unary_expr(self, orig_col: pl.Expr) -> pl.Expr:
    return orig_col.map(lambda s: talib.DEMA(s, timeperiod=self.timeperiod))

  def _feature_names(self) -> list[str]:
    return [f'DEMA({self.timeperiod})({self.col_feature.feature_name})']
