import polars as pl

from declafe.pl.feature_gen.tri.tri_feature import TriFeature
from declafe.pl.feature_gen import ColLike


class CondFeature(TriFeature):

  def __init__(self, test: ColLike, true: ColLike, false: ColLike):
    super().__init__(test, true, false)

  def _tri_expr(self, col1: pl.Expr, col2: pl.Expr, col3: pl.Expr):
    return pl.when(col1).then(col2).otherwise(col3)

  def _feature_names(self) -> list[str]:
    return [
        "if", self.col1_feature.wrapped_feature_name, "then",
        self.col2_feature.wrapped_feature_name, "else",
        self.col3_feature.wrapped_feature_name
    ]
