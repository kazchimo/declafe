import polars as pl

from declafe.pl.feature_gen.binary.binary_feature import BinaryFeature


class NeFeature(BinaryFeature):

  def _binary_expr(self, left: pl.Expr, right: pl.Expr):
    return left != right

  def _feature_names(self) -> list[str]:
    return [
        self._left_wrapped_feature_name, "!=", self._right_wrapped_feature_name
    ]
