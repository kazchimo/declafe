import polars as pl

from ..unary_feature import UnaryFeature


class MonthFeature(UnaryFeature):

  def _unary_expr(self, orig_col: pl.Expr):
    return orig_col.dt.month()

  def _feature_names(self) -> list[str]:
    return [f"month({self.col_feature.feature_name})"]
