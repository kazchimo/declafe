from datetime import tzinfo

import pandas as pd
import pytz

from ..UnaryColumnFeature import UnaryColumnFeature

__all__ = ["WeekOfYearFeature"]


class WeekOfYearFeature(UnaryColumnFeature):

  def __init__(self,
               column_name: str,
               timezone: tzinfo = pytz.timezone("Asia/Tokyo")):
    super().__init__(column_name)
    self.timezone = timezone

  def gen_unary(self, ser: pd.Series) -> pd.Series:
    return ser.apply(lambda x: x.isocalendar()[1])

  @property
  def name(self) -> str:
    return f"week_of_year"
