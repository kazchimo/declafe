import polars as pl
from declafe.pl.feature_gen.types import ColLike
import talib
from typing import cast

from declafe.pl.feature_gen.tri.tri_feature import TriFeature


class STOCHF_0Feature(TriFeature):

  def __init__(self, high: ColLike, low: ColLike, close: ColLike,
               fastk_period: int, fastd_period: int, fastd_matype: int):
    super().__init__(high, low, close)
    self.fastk_period = fastk_period
    self.fastd_period = fastd_period
    self.fastd_matype = fastd_matype

  def _tri_expr(self, col1: pl.Expr, col2: pl.Expr, col3: pl.Expr) -> pl.Expr:
    return cast(pl.Expr, pl.struct([col1, col2, col3])).map(
        lambda s: talib.STOCHF(s.struct.field(self.col1_feature.feature_name),
                               s.struct.field(self.col2_feature.feature_name),
                               s.struct.field(self.col3_feature.feature_name),
                               fastk_period=self.fastk_period,
                               fastd_period=self.fastd_period,
                               fastd_matype=self.fastd_matype)[0])

  def _feature_names(self) -> list[str]:
    return [
        f'STOCHF_0({self.fastk_period}, {self.fastd_period}, {self.fastd_matype})({self.col1_feature.feature_name}, {self.col2_feature.feature_name}, {self.col3_feature.feature_name})'
    ]


class STOCHF_1Feature(TriFeature):

  def __init__(self, high: ColLike, low: ColLike, close: ColLike,
               fastk_period: int, fastd_period: int, fastd_matype: int):
    super().__init__(high, low, close)
    self.fastk_period = fastk_period
    self.fastd_period = fastd_period
    self.fastd_matype = fastd_matype

  def _tri_expr(self, col1: pl.Expr, col2: pl.Expr, col3: pl.Expr) -> pl.Expr:
    return cast(pl.Expr, pl.struct([col1, col2, col3])).map(
        lambda s: talib.STOCHF(s.struct.field(self.col1_feature.feature_name),
                               s.struct.field(self.col2_feature.feature_name),
                               s.struct.field(self.col3_feature.feature_name),
                               fastk_period=self.fastk_period,
                               fastd_period=self.fastd_period,
                               fastd_matype=self.fastd_matype)[1])

  def _feature_names(self) -> list[str]:
    return [
        f'STOCHF_1({self.fastk_period}, {self.fastd_period}, {self.fastd_matype})({self.col1_feature.feature_name}, {self.col2_feature.feature_name}, {self.col3_feature.feature_name})'
    ]
