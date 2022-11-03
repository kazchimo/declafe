from datetime import datetime

import numpy as np
import pandas as pd

from ..UnaryFeature import UnaryFeature

__all__ = ["DayOfWeekFeature"]


class DayOfWeekFeature(UnaryFeature):

  def gen_unary(self, ser: pd.Series) -> pd.Series:
    gen = np.frompyfunc(
        lambda x: datetime.utcfromtimestamp(x / 1000_000_000).weekday(), 1, 1)
    return gen(ser)

  @property
  def name(self) -> str:
    return f"day_of_week"
