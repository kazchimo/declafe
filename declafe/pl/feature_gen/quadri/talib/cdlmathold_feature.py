import polars as pl
from declafe.pl.feature_gen.types import ColLike
import talib
from typing import cast

from declafe.pl.feature_gen.quadri.quadri_feature import QuadriFeature


class CDLMATHOLDFeature(QuadriFeature):

  def __init__(self,
               open: ColLike,
               high: ColLike,
               low: ColLike,
               close: ColLike,
               penetration: float = 0):
    super().__init__(open, high, low, close)
    self.penetration = penetration

  def _quadri_expr(self, col1: pl.Expr, col2: pl.Expr, col3: pl.Expr,
                   col4: pl.Expr) -> pl.Expr:
    return cast(pl.Expr,
                pl.struct([col1, col2, col3,
                           col4])).map(lambda s: talib.CDLMATHOLD(
                               s.struct.field(self.col1_feature.feature_name),
                               s.struct.field(self.col2_feature.feature_name),
                               s.struct.field(self.col3_feature.feature_name),
                               s.struct.field(self.col4_feature.feature_name),
                               penetration=self.penetration))

  def _feature_names(self) -> list[str]:
    return [
        f'CDLMATHOLD({self.penetration})({self.col1_feature.feature_name}, {self.col2_feature.feature_name}, {self.col3_feature.feature_name}, {self.col4_feature.feature_name})'
    ]
