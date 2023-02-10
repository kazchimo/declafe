import polars as pl
from declafe.pl.feature_gen.types import ColLike
import talib

from declafe.pl.feature_gen.unary.unary_feature import UnaryFeature


class MAFeature(UnaryFeature):

  def __init__(self, close: ColLike, timeperiod: int, matype: int):
    super().__init__(close)
    self.timeperiod = timeperiod
    self.matype = matype

  def _unary_expr(self, orig_col: pl.Expr) -> pl.Expr:
    return orig_col.map(
        lambda s: talib.MA(s, timeperiod=self.timeperiod, matype=self.matype))

  def _feature_names(self) -> list[str]:
    return [
        f'MA({self.timeperiod}, {self.matype})({self.col_feature.feature_name})'
    ]
