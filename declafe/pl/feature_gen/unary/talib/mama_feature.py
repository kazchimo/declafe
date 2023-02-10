import polars as pl
from declafe.pl.feature_gen.types import ColLike
import talib

from declafe.pl.feature_gen.unary.unary_feature import UnaryFeature


class MAMA_0Feature(UnaryFeature):

  def __init__(self, close: ColLike, fastlimit: float, slowlimit: float):
    super().__init__(close)
    self.fastlimit = fastlimit
    self.slowlimit = slowlimit

  def _unary_expr(self, orig_col: pl.Expr) -> pl.Expr:
    return orig_col.map(lambda s: talib.MAMA(
        s, fastlimit=self.fastlimit, slowlimit=self.slowlimit)[0])

  def _feature_names(self) -> list[str]:
    return [
        f'MAMA_0({self.fastlimit}, {self.slowlimit})({self.col_feature.feature_name})'
    ]


class MAMA_1Feature(UnaryFeature):

  def __init__(self, close: ColLike, fastlimit: float, slowlimit: float):
    super().__init__(close)
    self.fastlimit = fastlimit
    self.slowlimit = slowlimit

  def _unary_expr(self, orig_col: pl.Expr) -> pl.Expr:
    return orig_col.map(lambda s: talib.MAMA(
        s, fastlimit=self.fastlimit, slowlimit=self.slowlimit)[1])

  def _feature_names(self) -> list[str]:
    return [
        f'MAMA_1({self.fastlimit}, {self.slowlimit})({self.col_feature.feature_name})'
    ]
