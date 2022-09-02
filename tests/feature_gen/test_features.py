import pandas as pd

from declafe import cols, Features
from declafe.feature_gen.unary import SumFeature

test_df = pd.DataFrame({
    "a": list(range(1, 1001)),
    "b": list(range(1001, 2001))
})


class TestMap:

  def test_return_mapped_values(self):
    fs = cols(["a", "b"]).map(SumFeature, periods=2)
    df = test_df.copy()
    df = fs.set_features(df)

    assert df["sum_2_of_a"].equals(df["a"].rolling(2).sum())
    assert df["sum_2_of_b"].equals(df["b"].rolling(2).sum())

class TestIter:
  def test_iterate_over_inner_gen(self):
    fs = Features([c + 1 for c in cols(["a", "b"])])
    df = test_df.copy()
    df = fs.set_features(df)

    assert df["a_+_1"].equals(df["a"] + 1)
    assert df["b_+_1"].equals(df["b"] + 1)


