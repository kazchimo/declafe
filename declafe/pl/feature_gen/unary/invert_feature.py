import polars as pl

from declafe.pl.feature_gen.unary.unary_feature import UnaryFeature


class InvertFeature(UnaryFeature):

  def _unary_expr(self, orig_col: pl.Expr):
    return ~orig_col

  def _feature_names(self) -> list[str]:
    return [f"~{self._col_wrapped_feature_name}"]
