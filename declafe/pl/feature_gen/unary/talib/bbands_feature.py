import polars as pl
from declafe.pl.feature_gen.types import ColLike
import talib

from declafe.pl.feature_gen.unary.unary_feature import UnaryFeature


class BBANDS_0Feature(UnaryFeature):

  def __init__(self, close: ColLike, timeperiod: int, nbdevup: float,
               nbdevdn: float, matype: int):
    super().__init__(close)
    self.timeperiod = timeperiod
    self.nbdevup = nbdevup
    self.nbdevdn = nbdevdn
    self.matype = matype

  def _unary_expr(self, orig_col: pl.Expr) -> pl.Expr:
    return orig_col.map(lambda s: talib.BBANDS(s,
                                               timeperiod=self.timeperiod,
                                               nbdevup=self.nbdevup,
                                               nbdevdn=self.nbdevdn,
                                               matype=self.matype)[0])

  def _feature_names(self) -> list[str]:
    return [
        f'BBANDS_0({self.timeperiod}, {self.nbdevup}, {self.nbdevdn}, {self.matype})({self.col_feature.feature_name})'
    ]


class BBANDS_1Feature(UnaryFeature):

  def __init__(self, close: ColLike, timeperiod: int, nbdevup: float,
               nbdevdn: float, matype: int):
    super().__init__(close)
    self.timeperiod = timeperiod
    self.nbdevup = nbdevup
    self.nbdevdn = nbdevdn
    self.matype = matype

  def _unary_expr(self, orig_col: pl.Expr) -> pl.Expr:
    return orig_col.map(lambda s: talib.BBANDS(s,
                                               timeperiod=self.timeperiod,
                                               nbdevup=self.nbdevup,
                                               nbdevdn=self.nbdevdn,
                                               matype=self.matype)[1])

  def _feature_names(self) -> list[str]:
    return [
        f'BBANDS_1({self.timeperiod}, {self.nbdevup}, {self.nbdevdn}, {self.matype})({self.col_feature.feature_name})'
    ]


class BBANDS_2Feature(UnaryFeature):

  def __init__(self, close: ColLike, timeperiod: int, nbdevup: float,
               nbdevdn: float, matype: int):
    super().__init__(close)
    self.timeperiod = timeperiod
    self.nbdevup = nbdevup
    self.nbdevdn = nbdevdn
    self.matype = matype

  def _unary_expr(self, orig_col: pl.Expr) -> pl.Expr:
    return orig_col.map(lambda s: talib.BBANDS(s,
                                               timeperiod=self.timeperiod,
                                               nbdevup=self.nbdevup,
                                               nbdevdn=self.nbdevdn,
                                               matype=self.matype)[2])

  def _feature_names(self) -> list[str]:
    return [
        f'BBANDS_2({self.timeperiod}, {self.nbdevup}, {self.nbdevdn}, {self.matype})({self.col_feature.feature_name})'
    ]
