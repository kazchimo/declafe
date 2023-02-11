import polars as pl
from declafe.pl.feature_gen.types import ColLike
import talib
from typing import cast

from declafe.pl.feature_gen.tri.tri_feature import TriFeature


class STOCH_0Feature(TriFeature):

  def __init__(self, high: ColLike, low: ColLike, close: ColLike,
               fastk_period: int, slowk_period: int, slowk_matype: int,
               slowd_period: int, slowd_matype: int):
    super().__init__(high, low, close)
    self.fastk_period = fastk_period
    self.slowk_period = slowk_period
    self.slowk_matype = slowk_matype
    self.slowd_period = slowd_period
    self.slowd_matype = slowd_matype

  def _tri_expr(self, col1: pl.Expr, col2: pl.Expr, col3: pl.Expr) -> pl.Expr:
    return cast(pl.Expr, pl.struct([col1, col2, col3])).map(
        lambda s: talib.STOCH(s.struct.field(self.col1_feature.feature_name),
                              s.struct.field(self.col2_feature.feature_name),
                              s.struct.field(self.col3_feature.feature_name),
                              fastk_period=self.fastk_period,
                              slowk_period=self.slowk_period,
                              slowk_matype=self.slowk_matype,
                              slowd_period=self.slowd_period,
                              slowd_matype=self.slowd_matype)[0])

  def _feature_names(self) -> list[str]:
    return [
        f'STOCH_0({self.fastk_period}, {self.slowk_period}, {self.slowk_matype}, {self.slowd_period}, {self.slowd_matype})({self.col1_feature.feature_name}, {self.col2_feature.feature_name}, {self.col3_feature.feature_name})'
    ]


class STOCH_1Feature(TriFeature):

  def __init__(self, high: ColLike, low: ColLike, close: ColLike,
               fastk_period: int, slowk_period: int, slowk_matype: int,
               slowd_period: int, slowd_matype: int):
    super().__init__(high, low, close)
    self.fastk_period = fastk_period
    self.slowk_period = slowk_period
    self.slowk_matype = slowk_matype
    self.slowd_period = slowd_period
    self.slowd_matype = slowd_matype

  def _tri_expr(self, col1: pl.Expr, col2: pl.Expr, col3: pl.Expr) -> pl.Expr:
    return cast(pl.Expr, pl.struct([col1, col2, col3])).map(
        lambda s: talib.STOCH(s.struct.field(self.col1_feature.feature_name),
                              s.struct.field(self.col2_feature.feature_name),
                              s.struct.field(self.col3_feature.feature_name),
                              fastk_period=self.fastk_period,
                              slowk_period=self.slowk_period,
                              slowk_matype=self.slowk_matype,
                              slowd_period=self.slowd_period,
                              slowd_matype=self.slowd_matype)[1])

  def _feature_names(self) -> list[str]:
    return [
        f'STOCH_1({self.fastk_period}, {self.slowk_period}, {self.slowk_matype}, {self.slowd_period}, {self.slowd_matype})({self.col1_feature.feature_name}, {self.col2_feature.feature_name}, {self.col3_feature.feature_name})'
    ]
