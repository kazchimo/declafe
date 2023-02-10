import polars as pl
from declafe.pl.feature_gen.types import ColLike
import talib

from declafe.pl.feature_gen.unary.unary_feature import UnaryFeature


class MACDFIX_0Feature(UnaryFeature):

  def __init__(self, close: ColLike, signalperiod: int):
    super().__init__(close)
    self.signalperiod = signalperiod

  def _unary_expr(self, orig_col: pl.Expr) -> pl.Expr:
    return orig_col.map(
        lambda s: talib.MACDFIX(s, signalperiod=self.signalperiod)[0])

  def _feature_names(self) -> list[str]:
    return [f'MACDFIX_0({self.signalperiod})({self.col_feature.feature_name})']


class MACDFIX_1Feature(UnaryFeature):

  def __init__(self, close: ColLike, signalperiod: int):
    super().__init__(close)
    self.signalperiod = signalperiod

  def _unary_expr(self, orig_col: pl.Expr) -> pl.Expr:
    return orig_col.map(
        lambda s: talib.MACDFIX(s, signalperiod=self.signalperiod)[1])

  def _feature_names(self) -> list[str]:
    return [f'MACDFIX_1({self.signalperiod})({self.col_feature.feature_name})']


class MACDFIX_2Feature(UnaryFeature):

  def __init__(self, close: ColLike, signalperiod: int):
    super().__init__(close)
    self.signalperiod = signalperiod

  def _unary_expr(self, orig_col: pl.Expr) -> pl.Expr:
    return orig_col.map(
        lambda s: talib.MACDFIX(s, signalperiod=self.signalperiod)[2])

  def _feature_names(self) -> list[str]:
    return [f'MACDFIX_2({self.signalperiod})({self.col_feature.feature_name})']
