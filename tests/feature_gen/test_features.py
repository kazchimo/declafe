import pandas as pd

from declafe import cols, Features, c, col, FeatureGen
from declafe.feature_gen.unary import SumFeature, IdFeature

test_df = pd.DataFrame({
    "a": list(range(1, 1001)),
    "b": list(range(1001, 2001))
})

a = col("a")
b = col("b")


class TestInit:

  def test_remove_duplicated(self):
    assert Features([a, a]) == Features.one(a)


class TestSetFeatures:

  def test_return_calced_df(self):
    gen = (a + 1).to_features
    assert gen.set_features(test_df).equals(
        pd.DataFrame({
            "a": test_df["a"],
            "b": test_df["b"],
            "a_+_1": test_df["a"] + 1
        }))

  def test_not_calc_if_calced_once(self):

    class ThrowGen(FeatureGen):

      def gen(self, df: pd.DataFrame) -> pd.Series:
        raise Exception("Should not be called")

      def _feature_name(self) -> str:
        return "a_+_1"

    gen = Features([a + 1, ThrowGen()])

    gen.set_features(test_df)


class TestFeatureNames:

  def test_return_feature_names(self):
    assert Features([a + 1, b]).feature_names == ["a_+_1", "b"]


class TestUnaryFeatureNameOf:

  def test_return_feature_names_if_having_column(self):
    assert Features([a.lag(1), b]).unary_feature_name_of("a") == ["lag_1_of_a"]


class TestContains:

  def test_return_true_if_containing(self):
    assert (a + 1) in Features([a + 1, b])

  def test_return_false_if_not_containing(self):
    assert (a + 1) not in Features([a + 2, b])


class TestAdd:

  def test_return_new_features(self):
    assert Features([a + 1]) + Features([b]) == Features([a + 1, b])

  def test_return_new_features_if_containing(self):
    assert Features([a + 1]) + Features([a + 1]) == Features([a + 1])


class TestAddFeature:

  def test_return_new_features(self):
    assert Features([a + 1]).add_feature(b) == Features([a + 1, b])

  def test_return_new_features_if_containing(self):
    assert Features([a + 1]).add_feature(a + 1) == Features([a + 1])


class TestFilterByName:

  def test_return_filtered_features(self):
    assert Features([a + 1, b]).filter_by_name(["a_+_1"]) == Features([a + 1])


class TestFilterNotByName:

  def test_return_filtered_gen(self):
    fs = cols(["a", "b"]).filter_not_by_name(["a"])
    assert fs.feature_names == ["b"]


class TestMap:

  def test_return_mapped_values(self):
    fs = cols(["a", "b"]).map(SumFeature, periods=2)
    df = test_df.copy()
    df = fs.set_features(df)

    assert df["sum_2_of_a"].equals(df["a"].rolling(2).sum())
    assert df["sum_2_of_b"].equals(df["b"].rolling(2).sum())

  def test_map_by_func(self):
    fs = cols(["a", "b"]).map(lambda x: x + 1)
    df = test_df.copy()
    df = fs.set_features(df)

    assert df["a_+_1"].equals(df["a"] + 1)
    assert df["b_+_1"].equals(df["b"] + 1)


class TestFlatMap:

  def test_flat_map(self):
    fs = cols(["a", "b"]).flat_map(lambda x: [x + 1, x + 2])
    df = test_df.copy()
    df = fs.set_features(df)

    assert df["a_+_1"].equals(df["a"] + 1)
    assert df["a_+_2"].equals(df["a"] + 2)
    assert df["b_+_1"].equals(df["b"] + 1)
    assert df["b_+_2"].equals(df["b"] + 2)

  def test_flat_map_by_features(self):
    fs = cols(["a", "b"]).flat_map(lambda a: Features([a + 1, a + 2]))
    df = test_df.copy()
    df = fs.set_features(df)

    assert df["a_+_1"].equals(df["a"] + 1)
    assert df["a_+_2"].equals(df["a"] + 2)
    assert df["b_+_1"].equals(df["b"] + 1)
    assert df["b_+_2"].equals(df["b"] + 2)


class TestZipWith:

  def test_zip_with(self):
    df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6], "c": [7, 8, 9]})
    fs = cols(["a", "b"]).zip_with(cols(["b", "c"]), lambda f, ff: f + ff)
    df = fs.set_features(df)

    assert df["a_+_b"].equals(df["a"] + df["b"])
    assert df["b_+_c"].equals(df["b"] + df["c"])


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

    assert df["(0_+_a)_+_b"].equals(df["a"] + df["b"])


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


class TestFeatureCount:

  def test_return_feature_count(self):
    assert len(cols(["a", "b"])) == 2


class TestExtract:

  def test_extract(self):
    assert cols(["a", "b"]).extract(test_df).equals(test_df[["a", "b"]])


class TestAsTypeNumAll:

  def test_return_all_features_as_type_num(self):
    fs = Features.many(a.as_type("int64"), b).as_type_auto_num_all()
    df = fs.set_features(test_df.copy())

    assert df["a"].dtype == "int64"
    assert df["b"].dtype == "int16"

  def test_override(self):
    fs = Features.many(a.as_type("int64"), b).as_type_auto_num_all(True)
    df = fs.set_features(test_df.copy())

    assert df["a"].dtype == "int16"
    assert df["b"].dtype == "int16"


class TestStatic:

  class TestEmpty:

    def test_return_empty_features(self):
      assert Features.empty() == Features([])

  class TestOne:

    def test_return_one_features(self):
      assert Features.one(a) == Features([a])

  class TestTwo:

    def test_return_two_features(self):
      assert Features.two(a, b) == Features([a, b])

  class TestMany:

    def test_return_many_features(self):
      assert Features.many(a, b) == Features([a, b])
