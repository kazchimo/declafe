import polars as pl

from pl.feature_gen.unary.unary_feature import UnaryFeature
from pl.feature_gen.types import ColLike


class SumFeature(UnaryFeature):

  def __init__(self, periods: int, column: ColLike):
    super().__init__(column)
    self.periods = periods

  def _unary_expr(self, orig_col: pl.Expr):
    return orig_col.rolling_sum(self.periods)

  def _feature_name(self) -> str:
    return f"sum_{self.periods}_of_{self._wrapped_column_name}"
