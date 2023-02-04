import polars as pl

from pl.feature_gen.unary.unary_feature import UnaryFeature
from pl.feature_gen.types import ColLike


class PctChangeFeature(UnaryFeature):

  def __init__(self, periods: int, column: ColLike):
    super().__init__(column)
    self.periods = periods

  def _unary_expr(self, orig_col: pl.Expr):
    return orig_col.pct_change(self.periods)

  def _feature_names(self) -> list[str]:
    return [
        "pct_change",
        str(self.periods), "of", self._col_wrapped_feature_name
    ]
