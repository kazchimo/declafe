import polars as pl

from declafe.pl.feature_gen.unary.unary_feature import UnaryFeature


class AbsFeature(UnaryFeature):

  def _unary_expr(self, orig_col: pl.Expr):
    return orig_col.abs()

  def _feature_names(self) -> list[str]:
    return [f"|{self.col_feature.feature_name}|"]
