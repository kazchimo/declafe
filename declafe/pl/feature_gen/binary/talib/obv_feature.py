import polars as pl
from declafe.pl.feature_gen.types import ColLike
import talib
from typing import cast

from declafe.pl.feature_gen.binary.binary_feature import BinaryFeature


class OBVFeature(BinaryFeature):

  def __init__(self, close: ColLike, volume: ColLike):
    super().__init__(close, volume)

  def _binary_expr(self, left: pl.Expr, right: pl.Expr) -> pl.Expr:
    return cast(pl.Expr, pl.struct([left, right])).map(lambda s: talib.OBV(
        s.struct.field(self.left_feature.feature_name),
        s.struct.field(self.right_feature.feature_name),
    ))

  def _feature_names(self) -> list[str]:
    return [
        f'OBV()({self.left_feature.feature_name}, {self.right_feature.feature_name})'
    ]
