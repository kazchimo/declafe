import polars as pl

from ..unary_feature import UnaryFeature


class WeekOfYearFeature(UnaryFeature):

  def _unary_expr(self, orig_col: pl.Expr):
    return orig_col.dt.week()

  def _feature_names(self) -> list[str]:
    return [f"week_of_year({self.col_feature.feature_name})"]
