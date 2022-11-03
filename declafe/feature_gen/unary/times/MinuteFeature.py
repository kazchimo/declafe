from datetime import datetime

import numpy as np
import pandas as pd

from ..UnaryFeature import UnaryFeature

__all__ = ["MinuteFeature"]


class MinuteFeature(UnaryFeature):
  """対象カラムの分を抜き出す"""

  def gen_unary(self, ser: pd.Series) -> pd.Series:
    gen = np.frompyfunc(
        lambda x: datetime.utcfromtimestamp(x / 1000_000_000).minute, 1, 1)
    return gen(ser)

  @property
  def name(self) -> str:
    return f"minute"
