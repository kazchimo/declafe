import polars as pl
from declafe.pl.feature_gen.types import ColLike
import talib

from declafe.pl.feature_gen.unary.unary_feature import UnaryFeature


class STOCHRSI_0Feature(UnaryFeature):

  def __init__(self, close: ColLike, timeperiod: int, fastk_period: int,
               fastd_period: int, fastd_matype: int):
    super().__init__(close)
    self.timeperiod = timeperiod
    self.fastk_period = fastk_period
    self.fastd_period = fastd_period
    self.fastd_matype = fastd_matype

  def _unary_expr(self, orig_col: pl.Expr) -> pl.Expr:
    return orig_col.map(
        lambda s: talib.STOCHRSI(s,
                                 timeperiod=self.timeperiod,
                                 fastk_period=self.fastk_period,
                                 fastd_period=self.fastd_period,
                                 fastd_matype=self.fastd_matype)[0])

  def _feature_names(self) -> list[str]:
    return [
        f'STOCHRSI_0({self.timeperiod}, {self.fastk_period}, {self.fastd_period}, {self.fastd_matype})({self.col_feature.feature_name})'
    ]


class STOCHRSI_1Feature(UnaryFeature):

  def __init__(self, close: ColLike, timeperiod: int, fastk_period: int,
               fastd_period: int, fastd_matype: int):
    super().__init__(close)
    self.timeperiod = timeperiod
    self.fastk_period = fastk_period
    self.fastd_period = fastd_period
    self.fastd_matype = fastd_matype

  def _unary_expr(self, orig_col: pl.Expr) -> pl.Expr:
    return orig_col.map(
        lambda s: talib.STOCHRSI(s,
                                 timeperiod=self.timeperiod,
                                 fastk_period=self.fastk_period,
                                 fastd_period=self.fastd_period,
                                 fastd_matype=self.fastd_matype)[1])

  def _feature_names(self) -> list[str]:
    return [
        f'STOCHRSI_1({self.timeperiod}, {self.fastk_period}, {self.fastd_period}, {self.fastd_matype})({self.col_feature.feature_name})'
    ]
