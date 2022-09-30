from abc import ABC, abstractmethod

import pandas as pd

from declafe import FeatureGen, ColLike


class QuadriFeature(FeatureGen, ABC):

  def __init__(self, col1: ColLike, col2: ColLike, col3: ColLike,
               col4: ColLike):
    super().__init__()
    self.col1 = self.to_col(col1)
    self.col2 = self.to_col(col2)
    self.col3 = self.to_col(col3)
    self.col4 = self.to_col(col4)

  @abstractmethod
  def quadrigen(self, col1: pd.Series, col2: pd.Series, col3: pd.Series,
                col4: pd.Series) -> pd.Series:
    raise NotImplementedError()

  def gen(self, df: pd.DataFrame) -> pd.Series:
    return self.quadrigen(df[self.col1], df[self.col2], df[self.col3],
                          df[self.col4])
