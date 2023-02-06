import polars as pl
from pl.feature_gen.types import ColLike
import talib
from typing import cast

from pl.feature_gen.tri.tri_feature import TriFeature


class ADXFeature(TriFeature):

  def __init__(self, col1: ColLike, col2: ColLike, col3: ColLike,
               timeperiod: int):
    super().__init__(col1, col2, col3)
    self.timeperiod = timeperiod

  def _tri_expr(self, col1: pl.Expr, col2: pl.Expr, col3: pl.Expr) -> pl.Expr:
    return cast(pl.Expr, pl.struct([col1, col2, col3])).map(lambda s: talib.ADX(
        s.apply(lambda ss: ss[f'{self.col1_feature.feature_name}']),
        s.apply(lambda ss: ss[f'{self.col2_feature.feature_name}']),
        s.apply(lambda ss: ss[f'{self.col3_feature.feature_name}']),
        timeperiod=self.timeperiod))

  def _feature_names(self) -> list[str]:
    return [f'ADX({self.timeperiod})({self.col1}, {self.col2}, {self.col3})']
