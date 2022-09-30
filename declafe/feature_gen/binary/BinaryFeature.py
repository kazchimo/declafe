from abc import ABC, abstractmethod

import pandas as pd

from ..FeatureGen import FeatureGen, ColLike


class BinaryFeature(FeatureGen, ABC):

  def __init__(self, left: ColLike, right: ColLike):
    super().__init__()
    self.left = self.to_col(left)
    self.right = self.to_col(right)

  @abstractmethod
  def bigen(self, left: pd.Series, right: pd.Series) -> pd.Series:
    raise NotImplementedError()

  def gen(self, df: pd.DataFrame) -> pd.Series:
    return self.bigen(df[self.left], df[self.right])
