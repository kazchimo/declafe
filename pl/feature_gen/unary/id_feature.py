import polars as pl

from pl.feature_gen.unary.unary_feature import UnaryFeature


class IdFeature(UnaryFeature):

  def _unary_expr(self, orig_col: pl.Expr):
    return pl.col(self._wrapped_column_name)

  def _feature_name(self) -> str:
    if isinstance(self.column, str):
      return self.column
    else:
      return self._wrapped_column_name
