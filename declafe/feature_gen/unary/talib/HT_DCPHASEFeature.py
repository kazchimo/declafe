import pandas as pd
import talib

from declafe.feature_gen.unary import UnaryFeature


class HT_DCPHASEFeature(UnaryFeature):

  @property
  def name(self) -> str:
    return f"HT_DCPHASE"

  def gen_unary(self, ser: pd.Series) -> pd.Series:
    return talib.HT_DCPHASE(ser)
