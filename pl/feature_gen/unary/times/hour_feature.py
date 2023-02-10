import polars as pl

from ..unary_feature import UnaryFeature


class HourFeature(UnaryFeature):

  def _unary_expr(self, orig_col: pl.Expr):
    return orig_col.dt.hour()

  def _feature_names(self) -> list[str]:
    return [f"hour({self.col_feature.feature_name})"]
