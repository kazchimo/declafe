import polars as pl
from pl.feature_gen.types import ColLike
import talib
from typing import cast

from pl.feature_gen.binary.binary_feature import BinaryFeature


class AROON_0Feature(BinaryFeature):

  def __init__(self, left: ColLike, right: ColLike, timeperiod: int):
    super().__init__(left, right)
    self.timeperiod = timeperiod

  def _binary_expr(self, left: pl.Expr, right: pl.Expr) -> pl.Expr:
    return cast(pl.Expr, pl.struct([left, right])).map(lambda s: talib.AROON(
        s.apply(lambda ss: ss[f'{self.left_feature.feature_name}']),
        s.apply(lambda ss: ss[f'{self.right_feature.feature_name}']),
        timeperiod=self.timeperiod)[0])

  def _feature_names(self) -> list[str]:
    return [f'AROON_0({self.timeperiod})({self.left}, {self.right})']


class AROON_1Feature(BinaryFeature):

  def __init__(self, left: ColLike, right: ColLike, timeperiod: int):
    super().__init__(left, right)
    self.timeperiod = timeperiod

  def _binary_expr(self, left: pl.Expr, right: pl.Expr) -> pl.Expr:
    return cast(pl.Expr, pl.struct([left, right])).map(lambda s: talib.AROON(
        s.apply(lambda ss: ss[f'{self.left_feature.feature_name}']),
        s.apply(lambda ss: ss[f'{self.right_feature.feature_name}']),
        timeperiod=self.timeperiod)[1])

  def _feature_names(self) -> list[str]:
    return [f'AROON_1({self.timeperiod})({self.left}, {self.right})']
