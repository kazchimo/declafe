import pandas as pd

__all__ = ["MinWithFeature"]

from declafe.feature_gen.binary.BinaryFeature import BinaryFeature
import numpy as np


class MinWithFeature(BinaryFeature):

  def bigen(self, left: pd.Series, right: pd.Series) -> pd.Series:
    return np.minimum(left, right)

  def _feature_name(self) -> str:
    return f"{self.left}_min_with_{self.right}"
