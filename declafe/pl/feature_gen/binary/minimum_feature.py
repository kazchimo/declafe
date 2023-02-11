import polars as pl

from declafe.pl.feature_gen.binary.binary_feature import BinaryFeature


class MinimumFeature(BinaryFeature):

  def _binary_expr(self, left: pl.Expr, right: pl.Expr):
    return pl.when(left < right).then(left).otherwise(right)

  def _feature_names(self) -> list[str]:
    return [
        f"minimum({self.left_feature.feature_name}, {self.right_feature.feature_name})"
    ]
