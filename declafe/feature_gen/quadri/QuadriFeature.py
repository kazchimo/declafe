from abc import ABC, abstractmethod

import numpy as np
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
  def quadrigen(self, col1: np.ndarray, col2: np.ndarray, col3: np.ndarray,
                col4: np.ndarray) -> np.ndarray:
    raise NotImplementedError()

  def _gen(self, df: pd.DataFrame) -> np.ndarray:
    return self.quadrigen(df[self.col1].to_numpy(), df[self.col2].to_numpy(),
                          df[self.col3].to_numpy(), df[self.col4].to_numpy())
