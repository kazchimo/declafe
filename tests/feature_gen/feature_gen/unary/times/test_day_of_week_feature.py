from datetime import datetime

import pandas as pd

from declafe.feature_gen.unary.times import DayOfWeekFeature


class TestGen:

  def test_convert_to_day_of_week(self):
    df = pd.DataFrame({"date": [datetime(2020, 1, 1), datetime(2020, 1, 2)]})
    assert DayOfWeekFeature("date").gen(df).equals(pd.Series([2, 3]))
