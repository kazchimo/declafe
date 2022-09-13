import pandas as pd

from declafe import cols, Features, c, col
from declafe.feature_gen.unary import SumFeature, IdFeature

test_df = pd.DataFrame({
    "a": list(range(1, 1001)),
    "b": list(range(1001, 2001))
})

a = col("a")
b = col("b")


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

class TestReduce:
  def test_return_reduced_gen(self):
    fs = cols(["a", "b"]).reduce(lambda x, y: x + y, c(0)).to_features
    df = test_df.copy()
    df = fs.set_features(df)

    assert df["0_+_a_+_b"].equals(df["a"] + df["b"])

class TestFilterNotByName:
  def test_return_filtered_gen(self):
    fs = cols(["a", "b"]).filter_not_by_name(["a"])
    assert fs.feature_names == ["b"]

class TestFilterNot:
  def test_return_filtered_gen(self):
    fs = cols(["a", "b"]).filter_not([a])
    assert fs.feature_names == ["b"]

class TestFilterNotGen:
  def test_return_filtered_gen(self):
    fs = (cols(["a", "b"]).add_feature(c(1))).filter_not_gen(IdFeature)
    assert fs.feature_names == ["1"]

class TestFilter:
  def test_return_filtered_gen(self):
    fs = cols(["a", "b"]).filter([a])
    assert fs.feature_names == ["a"]

class TestFilterGen:
  def test_return_filtered_gen(self):
    fs = cols(["a", "b"]).add_feature(c(1)).filter_gen(IdFeature)
    assert fs.feature_names == ["a", "b"]
