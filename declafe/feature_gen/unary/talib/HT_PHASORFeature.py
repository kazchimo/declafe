import pandas as pd
import talib

from declafe.feature_gen.unary import UnaryColumnFeature


class HT_PHASORInphaseFeature(UnaryColumnFeature):

  @property
  def name(self) -> str:
    return f"HT_PHASOR_inphase"

  def gen_unary(self, ser: pd.Series) -> pd.Series:
    return talib.HT_PHASOR(ser)[0]


class HT_PHASORQuadratureFeature(UnaryColumnFeature):

  @property
  def name(self) -> str:
    return f"HT_PHASOR_quadrature"

  def gen_unary(self, ser: pd.Series) -> pd.Series:
    return talib.HT_PHASOR(ser)[1]
