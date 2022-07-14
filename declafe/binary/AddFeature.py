import pandas as pd

__all__ = ["AddFeature"]

from .BinaryFeature import BinaryFeature


class AddFeature(BinaryFeature):

  def bigen(self, left: pd.Series, right: pd.Series) -> pd.Series:
    return left + right

  def _feature_name(self) -> str:
    return f"{self.left}_+_{self.right}"
