import polars as pl

from ..unary_feature import UnaryFeature


class DayOfWeekFeature(UnaryFeature):

  def _unary_expr(self, orig_col: pl.Expr):
    return orig_col.dt.weekday()

  def _feature_names(self) -> list[str]:
    return [f"day_of_week({self.col_feature.feature_name})"]
