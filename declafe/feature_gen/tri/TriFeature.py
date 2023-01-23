from abc import ABC, abstractmethod

import numpy as np
import pandas as pd

from declafe import FeatureGen, ColLike


class TriFeature(FeatureGen, ABC):

  def __init__(self, col1: ColLike, col2: ColLike, col3: ColLike):
    super().__init__()
    self.col1 = self.to_col(col1)
    self.col2 = self.to_col(col2)
    self.col3 = self.to_col(col3)
    self.col1_f = self.to_col_feature_gen(col1)
    self.col2_f = self.to_col_feature_gen(col2)
    self.col3_f = self.to_col_feature_gen(col3)

  @abstractmethod
  def trigen(self, col1: np.ndarray, col2: np.ndarray,
             col3: np.ndarray) -> np.ndarray:
    raise NotImplementedError()

  def _gen(self, df: pd.DataFrame) -> np.ndarray:
    return self.trigen(
        self.col1_f.extract(df).to_numpy(),
        self.col2_f.extract(df).to_numpy(),
        self.col3_f.extract(df).to_numpy())
