from datetime import tzinfo, datetime

import numpy as np
import pytz

from ..UnaryFeature import UnaryFeature

__all__ = ["WeekOfYearFeature"]


class WeekOfYearFeature(UnaryFeature):

  def __init__(self,
               column_name: str,
               timezone: tzinfo = pytz.timezone("Asia/Tokyo")):
    super().__init__(column_name)
    self.timezone = timezone

  def gen_unary(self, ser: np.ndarray) -> np.ndarray:
    gen = np.frompyfunc(
        lambda x: datetime.utcfromtimestamp(x / 1000_000_000).isocalendar()[1],
        1, 1)

    return gen(ser).astype(np.int64)

  @property
  def name(self) -> str:
    return f"week_of_year"
