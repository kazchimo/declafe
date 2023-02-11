import polars as pl
from declafe.pl.feature_gen.types import ColLike
import talib
from typing import cast

from declafe.pl.feature_gen.quadri.quadri_feature import QuadriFeature


class CDLHARAMICROSSFeature(QuadriFeature):

  def __init__(self, open: ColLike, high: ColLike, low: ColLike,
               close: ColLike):
    super().__init__(open, high, low, close)

  def _quadri_expr(self, col1: pl.Expr, col2: pl.Expr, col3: pl.Expr,
                   col4: pl.Expr) -> pl.Expr:
    return cast(pl.Expr,
                pl.struct([col1, col2, col3,
                           col4])).map(lambda s: talib.CDLHARAMICROSS(
                               s.struct.field(self.col1_feature.feature_name),
                               s.struct.field(self.col2_feature.feature_name),
                               s.struct.field(self.col3_feature.feature_name),
                               s.struct.field(self.col4_feature.feature_name),
                           ))

  def _feature_names(self) -> list[str]:
    return [
        f'CDLHARAMICROSS()({self.col1_feature.feature_name}, {self.col2_feature.feature_name}, {self.col3_feature.feature_name}, {self.col4_feature.feature_name})'
    ]
