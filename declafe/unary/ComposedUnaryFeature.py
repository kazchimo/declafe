from typing import List

import pandas as pd

from .UnaryColumnFeature import UnaryColumnFeature

__all__ = ["ComposedUnaryFeature"]


class ComposedUnaryFeature(UnaryColumnFeature):

  def __init__(self, features: List[UnaryColumnFeature], column_name: str):
    if len(features) == 0:
      raise ValueError("featuresが空です")

    super().__init__(column_name)
    self.features = features

  @property
  def name(self) -> str:
    return f"composed_of_({'/'.join([f.name for f in self.features])})"

  def gen_unary(self, ser: pd.Series) -> pd.Series:
    result = ser

    for f in self.features:
      result = f.gen_unary(result)

    return result
