from datetime import datetime

import pandas as pd

from declafe.feature_gen.unary.times import MonthFeature


class TestGen:

  def test_convert_to_second(self):
    df = pd.DataFrame({"date": [datetime(2020, 1, 1), datetime(2020, 2, 1)]})
    assert MonthFeature("date").gen(df).equals(pd.Series([1, 2]))
