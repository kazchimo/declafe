import polars as pl

from ..unary_feature import UnaryFeature


class MinuteFeature(UnaryFeature):

  def _unary_expr(self, orig_col: pl.Expr):
    return orig_col.dt.minute()

  def _feature_names(self) -> list[str]:
    return [f"minute({self.col_feature.feature_name})"]
