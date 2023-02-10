import polars as pl

from declafe.pl.feature_gen.unary.unary_feature import UnaryFeature
from declafe.pl.feature_gen.types import ColLike


class LagFeature(UnaryFeature):

  def __init__(self, periods: int, column: ColLike):
    super().__init__(column)
    self.periods = periods

  def _unary_expr(self, orig_col: pl.Expr):
    return orig_col.shift(self.periods)

  def _feature_names(self) -> list[str]:
    return [f"lag{self.periods}({self.col_feature.feature_name})"]
