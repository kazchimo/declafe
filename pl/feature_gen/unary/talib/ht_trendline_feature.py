import polars as pl
from pl.feature_gen.types import ColLike
import talib

from pl.feature_gen.unary.unary_feature import UnaryFeature


class HT_TRENDLINEFeature(UnaryFeature):

  def __init__(self, column: ColLike):
    super().__init__(column)

  def _unary_expr(self, orig_col: pl.Expr) -> pl.Expr:
    return orig_col.map(lambda s: talib.HT_TRENDLINE(s,))

  def _feature_names(self) -> list[str]:
    return [f'HT_TRENDLINE()({self.column})']
