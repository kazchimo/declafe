import pandas as pd

__all__ = ["SubFeature"]

from lib.features.binary.BinaryFeature import BinaryFeature

class SubFeature(BinaryFeature):
  def bigen(self, left: pd.Series, right: pd.Series) -> pd.Series:
    return left - right

  def _feature_name(self) -> str:
    return f"{self.left}_-_{self.right}"
