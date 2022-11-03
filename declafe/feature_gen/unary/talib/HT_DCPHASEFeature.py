import numpy as np
import talib

from declafe.feature_gen.unary import UnaryFeature


class HT_DCPHASEFeature(UnaryFeature):

  @property
  def name(self) -> str:
    return f"HT_DCPHASE"

  def gen_unary(self, ser: np.ndarray) -> np.ndarray:
    return talib.HT_DCPHASE(ser.astype(float))
