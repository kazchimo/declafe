import pandas as pd

__all__ = ["MaxWithFeature"]

from declafe.feature_gen.binary.BinaryFeature import BinaryFeature
import numpy as np


class MaxWithFeature(BinaryFeature):

  def bigen(self, left: pd.Series, right: pd.Series) -> pd.Series:
    return np.maximum(left, right)

  def _feature_name(self) -> str:
    return f"{self.left}_max_with_{self.right}"
