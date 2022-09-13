import pandas as pd

__all__ = ["GEFeature"]

from ..BinaryFeature import BinaryFeature


class GEFeature(BinaryFeature):
  def bigen(self, left: pd.Series, right: pd.Series) -> pd.Series:
    return left >= right

  def _feature_name(self) -> str:
    return f"{self.left}_>=_{self.right}"
