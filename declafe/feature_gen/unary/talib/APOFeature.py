import pandas as pd
import talib

from ..UnaryColumnFeature import UnaryColumnFeature

__all__ = ["APOFeature"]


class APOFeature(UnaryColumnFeature):

  @property
  def name(self) -> str:
    return f"APO"

  def gen_unary(self, ser: pd.Series) -> pd.Series:
    return talib.APO(ser)
