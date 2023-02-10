import polars as pl

from declafe.pl.feature_gen.unary.unary_feature import UnaryFeature
from declafe.pl.feature_gen.types import ColLike


class RoundNFeature(UnaryFeature):

  def __init__(self, round_digit: int, column: ColLike):
    super().__init__(column)
    self.round_digit = round_digit

  def _unary_expr(self, orig_col: pl.Expr):
    return orig_col.round(self.round_digit)

  def _feature_names(self) -> list[str]:
    return [
        f"round{self.round_digit}({self.col_feature.feature_name})",
    ]
