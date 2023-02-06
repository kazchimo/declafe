import polars as pl
from pl.feature_gen.types import ColLike
import talib
from typing import cast

from pl.feature_gen.binary.binary_feature import BinaryFeature


class OBVFeature(BinaryFeature):

  def __init__(self, left: ColLike, right: ColLike):
    super().__init__(left, right)

  def _binary_expr(self, left: pl.Expr, right: pl.Expr) -> pl.Expr:
    return cast(pl.Expr, pl.struct([left, right])).map(lambda s: talib.OBV(
        s.apply(lambda ss: ss[f'{self.left_feature.feature_name}']),
        s.apply(lambda ss: ss[f'{self.right_feature.feature_name}']),
    ))

  def _feature_names(self) -> list[str]:
    return [f'OBV()({self.left}, {self.right})']
