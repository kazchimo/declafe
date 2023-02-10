import polars as pl
from declafe.pl.feature_gen.types import ColLike
import talib

from declafe.pl.feature_gen.unary.unary_feature import UnaryFeature


class MACD_0Feature(UnaryFeature):

  def __init__(self, close: ColLike, fastperiod: int, slowperiod: int,
               signalperiod: int):
    super().__init__(close)
    self.fastperiod = fastperiod
    self.slowperiod = slowperiod
    self.signalperiod = signalperiod

  def _unary_expr(self, orig_col: pl.Expr) -> pl.Expr:
    return orig_col.map(lambda s: talib.MACD(s,
                                             fastperiod=self.fastperiod,
                                             slowperiod=self.slowperiod,
                                             signalperiod=self.signalperiod)[0])

  def _feature_names(self) -> list[str]:
    return [
        f'MACD_0({self.fastperiod}, {self.slowperiod}, {self.signalperiod})({self.col_feature.feature_name})'
    ]


class MACD_1Feature(UnaryFeature):

  def __init__(self, close: ColLike, fastperiod: int, slowperiod: int,
               signalperiod: int):
    super().__init__(close)
    self.fastperiod = fastperiod
    self.slowperiod = slowperiod
    self.signalperiod = signalperiod

  def _unary_expr(self, orig_col: pl.Expr) -> pl.Expr:
    return orig_col.map(lambda s: talib.MACD(s,
                                             fastperiod=self.fastperiod,
                                             slowperiod=self.slowperiod,
                                             signalperiod=self.signalperiod)[1])

  def _feature_names(self) -> list[str]:
    return [
        f'MACD_1({self.fastperiod}, {self.slowperiod}, {self.signalperiod})({self.col_feature.feature_name})'
    ]


class MACD_2Feature(UnaryFeature):

  def __init__(self, close: ColLike, fastperiod: int, slowperiod: int,
               signalperiod: int):
    super().__init__(close)
    self.fastperiod = fastperiod
    self.slowperiod = slowperiod
    self.signalperiod = signalperiod

  def _unary_expr(self, orig_col: pl.Expr) -> pl.Expr:
    return orig_col.map(lambda s: talib.MACD(s,
                                             fastperiod=self.fastperiod,
                                             slowperiod=self.slowperiod,
                                             signalperiod=self.signalperiod)[2])

  def _feature_names(self) -> list[str]:
    return [
        f'MACD_2({self.fastperiod}, {self.slowperiod}, {self.signalperiod})({self.col_feature.feature_name})'
    ]
