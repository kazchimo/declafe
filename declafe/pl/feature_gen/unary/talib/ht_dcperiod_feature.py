import polars as pl
from declafe.pl.feature_gen.types import ColLike
import talib

from declafe.pl.feature_gen.unary.unary_feature import UnaryFeature


class HT_DCPERIODFeature(UnaryFeature):

  def __init__(self, close: ColLike):
    super().__init__(close)

  def _unary_expr(self, orig_col: pl.Expr) -> pl.Expr:
    return orig_col.map(lambda s: talib.HT_DCPERIOD(s,))

  def _feature_names(self) -> list[str]:
    return [f'HT_DCPERIOD()({self.col_feature.feature_name})']
