import pandas as pd
import talib

from declafe.feature_gen.unary import UnaryFeature


class HT_DCPERIODFeature(UnaryFeature):

  @property
  def name(self) -> str:
    return f"HT_DCPERIOD"

  def gen_unary(self, ser: pd.Series) -> pd.Series:
    return talib.HT_DCPERIOD(ser)
