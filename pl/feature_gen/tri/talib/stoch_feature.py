import polars as pl
from pl.feature_gen.types import ColLike
import talib
from typing import cast

from pl.feature_gen.tri.tri_feature import TriFeature


class STOCH_0Feature(TriFeature):

  def __init__(self, col1: ColLike, col2: ColLike, col3: ColLike,
               fastk_period: int, slowk_period: int, slowk_matype: int,
               slowd_period: int, slowd_matype: int):
    super().__init__(col1, col2, col3)
    self.fastk_period = fastk_period
    self.slowk_period = slowk_period
    self.slowk_matype = slowk_matype
    self.slowd_period = slowd_period
    self.slowd_matype = slowd_matype

  def _tri_expr(self, col1: pl.Expr, col2: pl.Expr, col3: pl.Expr) -> pl.Expr:
    return cast(pl.Expr,
                pl.struct([col1, col2, col3])).map(lambda s: talib.STOCH(
                    s.apply(lambda ss: ss[f'{self.col1_feature.feature_name}']),
                    s.apply(lambda ss: ss[f'{self.col2_feature.feature_name}']),
                    s.apply(lambda ss: ss[f'{self.col3_feature.feature_name}']),
                    fastk_period=self.fastk_period,
                    slowk_period=self.slowk_period,
                    slowk_matype=self.slowk_matype,
                    slowd_period=self.slowd_period,
                    slowd_matype=self.slowd_matype)[0])

  def _feature_names(self) -> list[str]:
    return [
        f'STOCH_0({self.fastk_period}, {self.slowk_period}, {self.slowk_matype}, {self.slowd_period}, {self.slowd_matype})({self.col1}, {self.col2}, {self.col3})'
    ]


class STOCH_1Feature(TriFeature):

  def __init__(self, col1: ColLike, col2: ColLike, col3: ColLike,
               fastk_period: int, slowk_period: int, slowk_matype: int,
               slowd_period: int, slowd_matype: int):
    super().__init__(col1, col2, col3)
    self.fastk_period = fastk_period
    self.slowk_period = slowk_period
    self.slowk_matype = slowk_matype
    self.slowd_period = slowd_period
    self.slowd_matype = slowd_matype

  def _tri_expr(self, col1: pl.Expr, col2: pl.Expr, col3: pl.Expr) -> pl.Expr:
    return cast(pl.Expr,
                pl.struct([col1, col2, col3])).map(lambda s: talib.STOCH(
                    s.apply(lambda ss: ss[f'{self.col1_feature.feature_name}']),
                    s.apply(lambda ss: ss[f'{self.col2_feature.feature_name}']),
                    s.apply(lambda ss: ss[f'{self.col3_feature.feature_name}']),
                    fastk_period=self.fastk_period,
                    slowk_period=self.slowk_period,
                    slowk_matype=self.slowk_matype,
                    slowd_period=self.slowd_period,
                    slowd_matype=self.slowd_matype)[1])

  def _feature_names(self) -> list[str]:
    return [
        f'STOCH_1({self.fastk_period}, {self.slowk_period}, {self.slowk_matype}, {self.slowd_period}, {self.slowd_matype})({self.col1}, {self.col2}, {self.col3})'
    ]
