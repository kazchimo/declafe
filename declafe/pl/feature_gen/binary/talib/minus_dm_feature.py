import polars as pl
from declafe.pl.feature_gen.types import ColLike
import talib
from typing import cast

from declafe.pl.feature_gen.binary.binary_feature import BinaryFeature


class MINUS_DMFeature(BinaryFeature):

  def __init__(self, low: ColLike, high: ColLike, timeperiod: int):
    super().__init__(low, high)
    self.timeperiod = timeperiod

  def _binary_expr(self, left: pl.Expr, right: pl.Expr) -> pl.Expr:
    return cast(pl.Expr, pl.struct([left, right])).map(lambda s: talib.MINUS_DM(
        s.struct.field(self.left_feature.feature_name),
        s.struct.field(self.right_feature.feature_name),
        timeperiod=self.timeperiod))

  def _feature_names(self) -> list[str]:
    return [
        f'MINUS_DM({self.timeperiod})({self.left_feature.feature_name}, {self.right_feature.feature_name})'
    ]
