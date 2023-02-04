import polars as pl

from pl.feature_gen.unary.unary_feature import UnaryFeature


class LogFeature(UnaryFeature):

  def _unary_expr(self, orig_col: pl.Expr):
    return orig_col.log()

  def _feature_name(self) -> str:
    return f"log({self.col_feature.feature_name})"
