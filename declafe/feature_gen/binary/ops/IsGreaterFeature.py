import pandas as pd

__all__ = ["IsGreaterFeature"]

from ..BinaryFeature import BinaryFeature


class IsGreaterFeature(BinaryFeature):
  """check if left is greater than right"""

  def bigen(self, left: pd.Series, right: pd.Series) -> pd.Series:
    return left > right

  def _feature_name(self) -> str:
    return f"{self.left}_>_{self.right}"
