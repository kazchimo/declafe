import pandas as pd
from datetime import datetime

from declafe.feature_gen.unary.times import WeekOfYearFeature


class TestGen:

  def test_week_of_year_feature(self):
    df = pd.DataFrame({"date": [datetime(2020, 1, 1), datetime(2020, 1, 8)]})
    assert WeekOfYearFeature("date").gen(df).equals(pd.Series([1, 2]))
