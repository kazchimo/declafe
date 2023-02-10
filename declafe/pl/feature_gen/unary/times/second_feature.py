import polars as pl

from ..unary_feature import UnaryFeature


class SecondFeature(UnaryFeature):

  def _unary_expr(self, orig_col: pl.Expr):
    return orig_col.dt.second()

  def _feature_names(self) -> list[str]:
    return [f"second({self.col_feature.feature_name})"]
