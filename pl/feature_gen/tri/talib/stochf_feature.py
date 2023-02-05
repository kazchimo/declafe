import polars as pl
from pl.feature_gen.types import ColLike
import talib
from pl.feature_gen.tri.tri_feature import TriFeature


class STOCHF_0Feature(TriFeature):

  def __init__(self, col1: ColLike, col2: ColLike, col3: ColLike,
               fastk_period: int, fastd_period: int, fastd_matype: int):
    super().__init__(col1, col2, col3)
    self.fastk_period = fastk_period
    self.fastd_period = fastd_period
    self.fastd_matype = fastd_matype

  def _tri_expr(self, col1: pl.Expr, col2: pl.Expr, col3: pl.Expr) -> pl.Expr:
    return pl.struct(
        [col1, col2,
         col3]).map(lambda s: talib.STOCHF(s[f'{self.col1.feature_name}'],
                                           s[f'{self.col2.feature_name}'],
                                           s[f'{self.col3.feature_name}'],
                                           fastk_period=self.fastk_period,
                                           fastd_period=self.fastd_period,
                                           fastd_matype=self.fastd_matype)[0])

  def _feature_names(self) -> list[str]:
    return [
        f'STOCHF_0({self.fastk_period}, {self.fastd_period}, {self.fastd_matype})({self.col1}, {self.col2}, {self.col3})'
    ]


class STOCHF_1Feature(TriFeature):

  def __init__(self, col1: ColLike, col2: ColLike, col3: ColLike,
               fastk_period: int, fastd_period: int, fastd_matype: int):
    super().__init__(col1, col2, col3)
    self.fastk_period = fastk_period
    self.fastd_period = fastd_period
    self.fastd_matype = fastd_matype

  def _tri_expr(self, col1: pl.Expr, col2: pl.Expr, col3: pl.Expr) -> pl.Expr:
    return pl.struct(
        [col1, col2,
         col3]).map(lambda s: talib.STOCHF(s[f'{self.col1.feature_name}'],
                                           s[f'{self.col2.feature_name}'],
                                           s[f'{self.col3.feature_name}'],
                                           fastk_period=self.fastk_period,
                                           fastd_period=self.fastd_period,
                                           fastd_matype=self.fastd_matype)[1])

  def _feature_names(self) -> list[str]:
    return [
        f'STOCHF_1({self.fastk_period}, {self.fastd_period}, {self.fastd_matype})({self.col1}, {self.col2}, {self.col3})'
    ]
