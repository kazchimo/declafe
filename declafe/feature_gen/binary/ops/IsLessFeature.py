import pandas as pd

__all__ = ["IsLessFeature"]

from ..BinaryFeature import BinaryFeature


class IsLessFeature(BinaryFeature):
  """check if left is greater than right"""

  def gen(self, df: pd.DataFrame) -> pd.Series:
    return df[self.left] < df[self.right]

  def bigen(self, left: pd.Series, right: pd.Series) -> pd.Series:
    return left < right

  def _feature_name(self) -> str:
    return f"{self.left}_<_{self.right}"
