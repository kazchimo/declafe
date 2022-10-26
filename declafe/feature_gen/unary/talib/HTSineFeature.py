import pandas as pd
import talib

from declafe.feature_gen.unary import UnaryFeature


class HTSineFeature(UnaryFeature):

  @property
  def name(self) -> str:
    return f"HT_SINE"

  def gen_unary(self, ser: pd.Series) -> pd.Series:
    return talib.HT_SINE(ser)[0]


class HTLeadsineFeature(UnaryFeature):

  @property
  def name(self) -> str:
    return f"HT_LEADSINE"

  def gen_unary(self, ser: pd.Series) -> pd.Series:
    return talib.HT_SINE(ser)[1]
