import numpy as np
import pandas as pd

from declafe.agg_feature_gen.agg_fun import DiffAtAgg


class TestCall:

  def test_return_diff(self):
    assert DiffAtAgg("a", 1)(pd.Series([2, 4, 8, 16])) == 2

  def test_return_nan_if_at_is_greater_than_size(self):
    assert np.isnan(DiffAtAgg("a", 3)(pd.Series([2, 4, 8])))
