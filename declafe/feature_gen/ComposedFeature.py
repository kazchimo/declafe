from typing import List, TYPE_CHECKING, Optional

import pandas as pd

from declafe.feature_gen import FeatureGen

__all__ = ["ComposedFeature"]

if TYPE_CHECKING:
  from declafe.feature_gen.unary.UnaryColumnFeature import UnaryFeature


class ComposedFeature(FeatureGen):

  def __init__(self, head: FeatureGen, nexts: List["UnaryFeature"]):
    self.head = head
    self.nexts = nexts
    super().__init__()

  def __post_init__(self):
    if len(self.nexts) == 0:
      raise ValueError("nextsが空です")

  def gen(self, df: pd.DataFrame) -> pd.Series:
    result = self.head.generate(df)
    df[self.head.feature_name] = result

    for i, f in enumerate(self.nexts):
      if f.feature_name in df.columns:
        result = df[f.feature_name]
      else:
        result = f.gen_unary(result)

        if i != len(self.nexts) - 1:
          df[f.feature_name] = result

    return result

  def _feature_name(self) -> str:
    return self.nexts[-1].feature_name
