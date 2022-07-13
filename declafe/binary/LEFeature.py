import re
from dataclasses import dataclass

import pandas as pd

from lib.features import FeatureGen

__all__ = ["LEFeature"]

from lib.features.binary.BinaryFeature import BinaryFeature

regex = "(\w+)_is_less_than_equal_(\w+)"

@dataclass
class LEFeature(BinaryFeature):
  left: str
  right: str

  def bigen(self, left: pd.Series, right: pd.Series) -> pd.Series:
    return left <= right

  def _feature_name(self) -> str:
    return f"{self.left}_is_less_than_equal_{self.right}"

  @staticmethod
  def serial_num() -> int:
    return 24

  @staticmethod
  def parse(s: str) -> "FeatureGen":
    match = re.match(regex, s)
    if match is None:
      raise ValueError(f"{s}は正しい形式ではありません")
    return LEFeature(left=match.group(1), right=match.group(2))
