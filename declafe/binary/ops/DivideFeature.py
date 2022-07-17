import pandas as pd

__all__ = ["DivideFeature"]

from ..BinaryFeature import BinaryFeature


class DivideFeature(BinaryFeature):

  def __init__(self, left: str, right: str, avoid_zero=True):
    super().__init__(left, right)
    self.left = left
    self.right = right
    self.avoid_zero = avoid_zero

  def bigen(self, left: pd.Series, right: pd.Series) -> pd.Series:
    if self.avoid_zero:
      right = right.replace(0, 1e-10)

    if (right == 0).any():
      raise ValueError(f"{self.right}に0が含まれています")

    return left / right

  def _feature_name(self) -> str:
    return f"{self.left}_/_{self.right}"
