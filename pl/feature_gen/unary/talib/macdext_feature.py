import polars as pl
from pl.feature_gen.types import ColLike
import talib

from pl.feature_gen.unary.unary_feature import UnaryFeature


class MACDEXT_0Feature(UnaryFeature):

  def __init__(self, column: ColLike, fastperiod: int, fastmatype: int,
               slowperiod: int, slowmatype: int, signalperiod: int,
               signalmatype: int):
    super().__init__(column)
    self.fastperiod = fastperiod
    self.fastmatype = fastmatype
    self.slowperiod = slowperiod
    self.slowmatype = slowmatype
    self.signalperiod = signalperiod
    self.signalmatype = signalmatype

  def _unary_expr(self, orig_col: pl.Expr) -> pl.Expr:
    return orig_col.map(
        lambda s: talib.MACDEXT(s,
                                fastperiod=self.fastperiod,
                                fastmatype=self.fastmatype,
                                slowperiod=self.slowperiod,
                                slowmatype=self.slowmatype,
                                signalperiod=self.signalperiod,
                                signalmatype=self.signalmatype)[0])

  def _feature_names(self) -> list[str]:
    return [
        f'MACDEXT_0({self.fastperiod}, {self.fastmatype}, {self.slowperiod}, {self.slowmatype}, {self.signalperiod}, {self.signalmatype})({self.column})'
    ]


class MACDEXT_1Feature(UnaryFeature):

  def __init__(self, column: ColLike, fastperiod: int, fastmatype: int,
               slowperiod: int, slowmatype: int, signalperiod: int,
               signalmatype: int):
    super().__init__(column)
    self.fastperiod = fastperiod
    self.fastmatype = fastmatype
    self.slowperiod = slowperiod
    self.slowmatype = slowmatype
    self.signalperiod = signalperiod
    self.signalmatype = signalmatype

  def _unary_expr(self, orig_col: pl.Expr) -> pl.Expr:
    return orig_col.map(
        lambda s: talib.MACDEXT(s,
                                fastperiod=self.fastperiod,
                                fastmatype=self.fastmatype,
                                slowperiod=self.slowperiod,
                                slowmatype=self.slowmatype,
                                signalperiod=self.signalperiod,
                                signalmatype=self.signalmatype)[1])

  def _feature_names(self) -> list[str]:
    return [
        f'MACDEXT_1({self.fastperiod}, {self.fastmatype}, {self.slowperiod}, {self.slowmatype}, {self.signalperiod}, {self.signalmatype})({self.column})'
    ]


class MACDEXT_2Feature(UnaryFeature):

  def __init__(self, column: ColLike, fastperiod: int, fastmatype: int,
               slowperiod: int, slowmatype: int, signalperiod: int,
               signalmatype: int):
    super().__init__(column)
    self.fastperiod = fastperiod
    self.fastmatype = fastmatype
    self.slowperiod = slowperiod
    self.slowmatype = slowmatype
    self.signalperiod = signalperiod
    self.signalmatype = signalmatype

  def _unary_expr(self, orig_col: pl.Expr) -> pl.Expr:
    return orig_col.map(
        lambda s: talib.MACDEXT(s,
                                fastperiod=self.fastperiod,
                                fastmatype=self.fastmatype,
                                slowperiod=self.slowperiod,
                                slowmatype=self.slowmatype,
                                signalperiod=self.signalperiod,
                                signalmatype=self.signalmatype)[2])

  def _feature_names(self) -> list[str]:
    return [
        f'MACDEXT_2({self.fastperiod}, {self.fastmatype}, {self.slowperiod}, {self.slowmatype}, {self.signalperiod}, {self.signalmatype})({self.column})'
    ]
