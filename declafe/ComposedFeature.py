from typing import List

import pandas as pd

from declafe.feature_gen import *
from declafe.unary.UnaryColumnFeature import UnaryColumnFeature

__all__ = ["ComposedFeature"]

class ComposedFeature(FeatureGen):

  def __init__(self, head: FeatureGen, nexts: List[UnaryColumnFeature]):
    self.head = head
    self.nexts = nexts
    super().__init__()

  def __post_init__(self):
    if len(self.nexts) == 0:
      raise ValueError("nextsが空です")

  def gen(self, df: pd.DataFrame) -> pd.Series:
    result = self.head.generate(df)

    for f in self.nexts:
      result = f.gen_unary(result)

    return result

  def _feature_name(self) -> str:
    return self.nexts[-1].feature_name

  @staticmethod
  def chain(first: FeatureGen, second: FeatureGen) -> "ComposedFeature":
    return ComposedFeature(head=first, nexts=[second])
