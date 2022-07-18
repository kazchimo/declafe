from abc import ABC, abstractmethod

import pandas as pd

from ..FeatureGen import FeatureGen


class BinaryFeature(FeatureGen, ABC):

  def __init__(self, left: str, right: str):
    super().__init__()
    self.left = left
    self.right = right

  @abstractmethod
  def bigen(self, left: pd.Series, right: pd.Series) -> pd.Series:
    raise NotImplementedError()

  def gen(self, df: pd.DataFrame) -> pd.Series:
    return self.bigen(df[self.left], df[self.right])
