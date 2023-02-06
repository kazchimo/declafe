import polars as pl
from pl.feature_gen.types import ColLike
import talib
from typing import cast

from pl.feature_gen.binary.binary_feature import BinaryFeature


class BETAFeature(BinaryFeature):

  def __init__(self, left: ColLike, right: ColLike, timeperiod: int):
    super().__init__(left, right)
    self.timeperiod = timeperiod

  def _binary_expr(self, left: pl.Expr, right: pl.Expr) -> pl.Expr:
    return cast(pl.Expr, pl.struct([left, right])).map(lambda s: talib.BETA(
        s.apply(lambda ss: ss[f'{self.left_feature.feature_name}']),
        s.apply(lambda ss: ss[f'{self.right_feature.feature_name}']),
        timeperiod=self.timeperiod))

  def _feature_names(self) -> list[str]:
    return [f'BETA({self.timeperiod})({self.left}, {self.right})']
