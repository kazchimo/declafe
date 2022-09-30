from typing import Union

import pandas as pd
import talib

from declafe import ColLike
from declafe.feature_gen import FeatureGen

__all__ = ["MinusDIFeature"]

from declafe.feature_gen.tri.TriFeature import TriFeature

C = Union[FeatureGen, str]


class MinusDIFeature(TriFeature):

  def __init__(self, high: ColLike, low: ColLike, close: ColLike, period: int):
    super().__init__(high, low, close)
    self.period = period

  def trigen(self, col1: pd.Series, col2: pd.Series,
             col3: pd.Series) -> pd.Series:
    return talib.MINUS_DI(col1, col2, col3, self.period)

  def _feature_name(self) -> str:
    return f"MINUS_DI_{self.period}_of_{self.col1}_{self.col2}_{self.col3}"
