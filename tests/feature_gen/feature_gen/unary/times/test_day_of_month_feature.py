from datetime import datetime

import pandas as pd

from declafe.feature_gen.unary.times import DayOfMonthFeature


class TestGen:

  def test_convert_to_day_of_month(self):
    df = pd.DataFrame({"date": [datetime(2020, 1, 1), datetime(2020, 1, 15)]})
    assert DayOfMonthFeature("date").gen(df).equals(pd.Series([1, 15]))
