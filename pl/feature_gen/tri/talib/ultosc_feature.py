import polars as pl
from pl.feature_gen.types import ColLike
import talib
from typing import cast

from pl.feature_gen.tri.tri_feature import TriFeature


class ULTOSCFeature(TriFeature):

  def __init__(self,
               col1: ColLike,
               col2: ColLike,
               col3: ColLike,
               timeperiod1: int = 7,
               timeperiod2: int = 14,
               timeperiod3: int = 28):
    super().__init__(col1, col2, col3)
    self.timeperiod1 = timeperiod1
    self.timeperiod2 = timeperiod2
    self.timeperiod3 = timeperiod3

  def _tri_expr(self, col1: pl.Expr, col2: pl.Expr, col3: pl.Expr) -> pl.Expr:
    return cast(pl.Expr,
                pl.struct([col1, col2, col3])).map(lambda s: talib.ULTOSC(
                    s.apply(lambda ss: ss[f'{self.col1_feature.feature_name}']),
                    s.apply(lambda ss: ss[f'{self.col2_feature.feature_name}']),
                    s.apply(lambda ss: ss[f'{self.col3_feature.feature_name}']),
                    timeperiod1=self.timeperiod1,
                    timeperiod2=self.timeperiod2,
                    timeperiod3=self.timeperiod3))

  def _feature_names(self) -> list[str]:
    return [
        f'ULTOSC({self.timeperiod1}, {self.timeperiod2}, {self.timeperiod3})({self.col1}, {self.col2}, {self.col3})'
    ]
