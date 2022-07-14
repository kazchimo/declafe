from dataclasses import dataclass
from datetime import tzinfo

import pandas as pd
import pytz

from ..UnaryColumnFeature import UnaryColumnFeature

__all__ = ["WeekOfYearFeature"]


@dataclass
class WeekOfYearFeature(UnaryColumnFeature):
  timezone: tzinfo = pytz.timezone("Asia/Tokyo")

  def gen_unary(self, ser: pd.Series) -> pd.Series:
    return ser.apply(lambda x: x.isocalendar()[1])

  @property
  def name(self) -> str:
    return f"week_of_year"
