import polars as pl
from declafe.pl.feature_gen.types import ColLike
import talib

from declafe.pl.feature_gen.unary.unary_feature import UnaryFeature


class HT_PHASOR_0Feature(UnaryFeature):

  def __init__(self, close: ColLike):
    super().__init__(close)

  def _unary_expr(self, orig_col: pl.Expr) -> pl.Expr:
    return orig_col.map(lambda s: talib.HT_PHASOR(s,)[0])

  def _feature_names(self) -> list[str]:
    return [f'HT_PHASOR_0()({self.col_feature.feature_name})']


class HT_PHASOR_1Feature(UnaryFeature):

  def __init__(self, close: ColLike):
    super().__init__(close)

  def _unary_expr(self, orig_col: pl.Expr) -> pl.Expr:
    return orig_col.map(lambda s: talib.HT_PHASOR(s,)[1])

  def _feature_names(self) -> list[str]:
    return [f'HT_PHASOR_1()({self.col_feature.feature_name})']
