import pandas as pd
import talib

from declafe.feature_gen.unary import UnaryColumnFeature


class HT_DCPHASEFeature(UnaryColumnFeature):

  @property
  def name(self) -> str:
    return f"HT_DCPHASE"

  def gen_unary(self, ser: pd.Series) -> pd.Series:
    return talib.HT_DCPHASE(ser)
