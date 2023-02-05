import polars as pl
from pl.feature_gen.types import ColLike
import talib
from pl.feature_gen.binary.binary_feature import BinaryFeature


class MIDPRICEFeature(BinaryFeature):

  def __init__(self, left: ColLike, right: ColLike, timeperiod: int):
    super().__init__(left, right)
    self.timeperiod = timeperiod

  def _binary_expr(self, left: pl.Expr, right: pl.Expr) -> pl.Expr:
    return pl.struct(
        [left,
         right]).map(lambda s: talib.MIDPRICE(s[f'{self.left.feature_name}'],
                                              s[f'{self.right.feature_name}'],
                                              timeperiod=self.timeperiod))

  def _feature_names(self) -> list[str]:
    return [f'MIDPRICE({self.timeperiod})({self.left}, {self.right})']
