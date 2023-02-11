import polars as pl
from declafe.pl.feature_gen.types import ColLike
import talib
from typing import cast

from declafe.pl.feature_gen.binary.binary_feature import BinaryFeature


class SARFeature(BinaryFeature):

  def __init__(self, high: ColLike, low: ColLike, acceleration: float,
               maximum: float):
    super().__init__(high, low)
    self.acceleration = acceleration
    self.maximum = maximum

  def _binary_expr(self, left: pl.Expr, right: pl.Expr) -> pl.Expr:
    return cast(pl.Expr, pl.struct([
        left, right
    ])).map(lambda s: talib.SAR(s.struct.field(self.left_feature.feature_name),
                                s.struct.field(self.right_feature.feature_name),
                                acceleration=self.acceleration,
                                maximum=self.maximum))

  def _feature_names(self) -> list[str]:
    return [
        f'SAR({self.acceleration}, {self.maximum})({self.left_feature.feature_name}, {self.right_feature.feature_name})'
    ]
