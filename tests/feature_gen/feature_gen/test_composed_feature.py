import numpy as np
import pandas as pd

from declafe import col

a = col("a")


class TestGen:

  def test_calc_all_for_plain_df(self):
    df = pd.DataFrame({"a": [1, 2, 3, 4, 5]})
    fs = a.moving_sum(2).moving_max(2).to_features

    result = fs.set_features(df)

    assert result.equals(
        pd.DataFrame({
            "a": [1, 2, 3, 4, 5],
            "sum_2_of_a": [np.nan, 3, 5, 7, 9],
            "max_2_of_sum_2_of_a": [np.nan, np.nan, 5, 7, 9]
        }))
