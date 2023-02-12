from typing import Protocol, Any

import polars as pl

from declafe.pl.feature_gen import ColLike
from declafe.pl.feature_gen.feature_gen import FeatureGen


class F(Protocol):

  def __call__(self, ser: pl.Series) -> Any:
    ...


class RollingApplyFeature(FeatureGen):

  def __init__(
      self,
      target_col: ColLike,
      window: int,
      f: F,
      ops_name: str,
  ):
    super(RollingApplyFeature, self).__init__()

    self.target_col = target_col
    self.window = window
    self.f = f
    self.ops_name = ops_name

  def _expr(self) -> pl.Expr:
    from declafe.pl.feature_gen import col_like_to_feature_gen
    return col_like_to_feature_gen(self.target_col).expr().rolling_apply(
        self.f, self.window)

  def _feature_names(self) -> list[str]:
    from declafe.pl.feature_gen import col_like_to_feature_gen

    return [
        "rolling_apply", self.ops_name, "over",
        col_like_to_feature_gen(self.target_col).wrapped_feature_name,
        str(self.window)
    ]

  @property
  def _target_col_feature_name(self) -> str:
    from declafe.pl.feature_gen import col_like_to_str
    return col_like_to_str(self.target_col)
