import pandas as pd
import talib

from declafe.feature_gen import FeatureGen


class BOPFeature(FeatureGen):

  def __init__(self, open_col: str, high_col: str, low_col: str,
               close_col: str):
    super().__init__()
    self.open_col = open_col
    self.high_col = high_col
    self.low_col = low_col
    self.close_col = close_col

  def gen(self, df: pd.DataFrame) -> pd.Series:
    return talib.BOP(df[self.open_col], df[self.high_col], df[self.low_col],
                     df[self.close_col])

  def _feature_name(self) -> str:
    return "BOP"
