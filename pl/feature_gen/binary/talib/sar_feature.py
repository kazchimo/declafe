import polars as pl
from pl.feature_gen.types import ColLike
import talib
from typing import cast

from pl.feature_gen.binary.binary_feature import BinaryFeature


class SARFeature(BinaryFeature):

  def __init__(self, left: ColLike, right: ColLike, acceleration: float,
               maximum: float):
    super().__init__(left, right)
    self.acceleration = acceleration
    self.maximum = maximum

  def _binary_expr(self, left: pl.Expr, right: pl.Expr) -> pl.Expr:
    return cast(pl.Expr, pl.struct([left, right])).map(lambda s: talib.SAR(
        s.apply(lambda ss: ss[f'{self.left_feature.feature_name}']),
        s.apply(lambda ss: ss[f'{self.right_feature.feature_name}']),
        acceleration=self.acceleration,
        maximum=self.maximum))

  def _feature_names(self) -> list[str]:
    return [
        f'SAR({self.acceleration}, {self.maximum})({self.left}, {self.right})'
    ]
