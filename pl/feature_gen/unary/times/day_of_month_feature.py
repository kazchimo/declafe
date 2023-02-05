import polars as pl

from ..unary_feature import UnaryFeature

__all__ = ["DayOfMonthFeature"]


class DayOfMonthFeature(UnaryFeature):

  def _unary_expr(self, orig_col: pl.Expr):
    return orig_col.dt.day()

  def _feature_names(self) -> list[str]:
    return [f"day_of_month({self.col_feature.feature_name})"]
