from datetime import datetime

import pandas as pd

from declafe.feature_gen.unary.times import SecondFeature


class TestGen:
  def test_convert_to_second(self):
    df = pd.DataFrame({"date": [datetime(2020, 1, 1, 0, 0, 1), datetime(2020, 1, 1, 0, 0, 2)]})
    assert SecondFeature("date").gen(df).equals(pd.Series([1, 2]))
