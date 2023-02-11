import polars as pl
from declafe.pl.feature_gen.types import ColLike
import talib
from typing import cast

from declafe.pl.feature_gen.binary.binary_feature import BinaryFeature


class BETAFeature(BinaryFeature):

  def __init__(self, high: ColLike, low: ColLike, timeperiod: int):
    super().__init__(high, low)
    self.timeperiod = timeperiod

  def _binary_expr(self, left: pl.Expr, right: pl.Expr) -> pl.Expr:
    return cast(pl.Expr, pl.struct([left, right])).map(
        lambda s: talib.BETA(s.struct.field(self.left_feature.feature_name),
                             s.struct.field(self.right_feature.feature_name),
                             timeperiod=self.timeperiod))

  def _feature_names(self) -> list[str]:
    return [
        f'BETA({self.timeperiod})({self.left_feature.feature_name}, {self.right_feature.feature_name})'
    ]
