import polars as pl

from pl.feature_gen.unary.unary_feature import UnaryFeature


class IdFeature(UnaryFeature):

  def _unary_expr(self, orig_col: pl.Expr):
    return orig_col

  def _feature_name(self) -> str:
    return self.column_name
