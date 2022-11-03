import numpy as np
import talib

from declafe.feature_gen.unary import UnaryFeature


class HT_DCPERIODFeature(UnaryFeature):

  @property
  def name(self) -> str:
    return f"HT_DCPERIOD"

  def gen_unary(self, ser: np.ndarray) -> np.ndarray:
    return talib.HT_DCPERIOD(ser.astype(float))
