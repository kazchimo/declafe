import polars as pl
from pl.feature_gen.types import ColLike
import talib
from typing import cast

from pl.feature_gen.quadri.quadri_feature import QuadriFeature


class MFIFeature(QuadriFeature):

  def __init__(self, high: ColLike, low: ColLike, close: ColLike,
               volume: ColLike, timeperiod: int):
    super().__init__(high, low, close, volume)
    self.timeperiod = timeperiod

  def _quadri_expr(self, col1: pl.Expr, col2: pl.Expr, col3: pl.Expr,
                   col4: pl.Expr) -> pl.Expr:
    return cast(pl.Expr,
                pl.struct([col1, col2, col3, col4])).map(lambda s: talib.MFI(
                    s.apply(lambda ss: ss[f'{self.col1_feature.feature_name}']),
                    s.apply(lambda ss: ss[f'{self.col2_feature.feature_name}']),
                    s.apply(lambda ss: ss[f'{self.col3_feature.feature_name}']),
                    s.apply(lambda ss: ss[f'{self.col4_feature.feature_name}']),
                    timeperiod=self.timeperiod))

  def _feature_names(self) -> list[str]:
    return [
        f'MFI({self.timeperiod})({self.col1}, {self.col2}, {self.col3}, {self.col4})'
    ]
