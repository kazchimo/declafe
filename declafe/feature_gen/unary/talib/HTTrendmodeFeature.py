import pandas as pd
import talib

from declafe.feature_gen.unary import UnaryFeature


class HTTrendModeFeature(UnaryFeature):

  @property
  def name(self) -> str:
    return f"HT_TRENDMODE"

  def gen_unary(self, ser: pd.Series) -> pd.Series:
    return talib.HT_TRENDMODE(ser)
