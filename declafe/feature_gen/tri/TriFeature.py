from abc import ABC, abstractmethod

import pandas as pd

from declafe import FeatureGen, ColLike


class TriFeature(FeatureGen, ABC):

  def __init__(self, col1: ColLike, col2: ColLike, col3: ColLike):
    super().__init__()
    self.col1 = self.to_col(col1)
    self.col2 = self.to_col(col2)
    self.col3 = self.to_col(col3)

  @abstractmethod
  def trigen(self, col1: pd.Series, col2: pd.Series,
             col3: pd.Series) -> pd.Series:
    raise NotImplementedError()

  def gen(self, df: pd.DataFrame) -> pd.Series:
    return self.trigen(df[self.col1], df[self.col2], df[self.col3])
