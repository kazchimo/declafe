from typing import Any

import polars as pl

from declafe.pl.feature_gen import FeatureGen


class ConstFeature(FeatureGen):

  def __init__(self, value: Any):
    super().__init__()
    self.value = value

  def _expr(self) -> pl.Expr:
    return pl.lit(self.value).alias(self.feature_name)

  def _feature_names(self) -> list[str]:
    return [str(self.value)]
