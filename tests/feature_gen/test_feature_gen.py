import numpy as np
import pandas as pd

from declafe import ConstFeature, Features
from declafe.feature_gen import FeatureGen
from declafe.feature_gen.dsl import c, col

test_df = pd.DataFrame({
    "a": list(range(1, 1001)),
    "b": list(range(1001, 2001))
})

a = col("a")
b = col("b")


class SimpleGen(FeatureGen):

  def _gen(self, df: pd.DataFrame) -> pd.Series:
    return pd.Series(1, index=df.index)

  def _feature_name(self) -> str:
    return "test_gen"


_1 = c(1)


class TestFeatureName:

  def test_return_pre_defined_name_if_not_overrode(self):
    gen = SimpleGen()
    assert gen.feature_name == "test_gen"

  def test_return_overrode_name(self):
    gen = SimpleGen()
    gen.as_name_of("overrode")
    assert gen.feature_name == "overrode"


class TestEquality:

  def test_equal_if_same_feature_name(self):
    gen1 = SimpleGen()
    gen2 = ConstFeature(1).as_name_of("test_gen")
    gen3 = ConstFeature(1)
    assert gen1.equals(gen2)
    assert not gen1.equals(gen3)


class TestInit:

  def test_remove_duplicated_gens(self):
    fs = Features(
        [SimpleGen(),
         ConstFeature(1),
         ConstFeature(2).as_name_of("test_gen")])

    assert fs.feature_count == 2
    assert fs.feature_names == ["test_gen", "1"]


class TestToStr:

  def test_to_str(self):
    f = SimpleGen()
    ff = ConstFeature(1)

    assert str(f) == "test_gen"
    assert str(ff) == "1"


class TestAsType:

  def test_as_type(self):
    f = SimpleGen().as_type("int8")
    ff = ConstFeature(1).as_type("category")

    assert f.generate(test_df).dtype == "int8"
    assert ff.generate(test_df).dtype == "int64"


class TestAsBool:

  def test_as_bool(self):
    f = SimpleGen().as_bool()
    ff = ConstFeature(1).as_bool()

    assert f.generate(test_df).dtype == "bool"
    assert ff.generate(test_df).dtype == "bool"


class TestAsTypeAutoNum:

  def test_as_type_auto_num(self):
    f = SimpleGen().as_type_auto_num()
    f2 = ConstFeature(2**8 + 1).as_type_auto_num()
    f3 = ConstFeature(2**16 + 1).as_type_auto_num()
    f4 = ConstFeature(2**32 + 1).as_type_auto_num()
    f5 = ConstFeature(2**8 + 0.1).as_type_auto_num()
    f6 = ConstFeature(np.finfo(np.float16).max + 1).as_type_auto_num()
    f7 = ConstFeature(np.finfo(np.float32).max + 1).as_type_auto_num()

    assert f.generate(test_df).dtype == "int8"
    assert f2.generate(test_df).dtype == "int16"
    assert f3.generate(test_df).dtype == "int32"
    assert f4.generate(test_df).dtype == "int64"
    assert f5.generate(test_df).dtype == "float16"
    assert f6.generate(test_df).dtype == "float32"
    assert f7.generate(test_df).dtype == "float64"

  def test_override(self):
    f = SimpleGen().as_type("float64").as_type_auto_num()
    f2 = SimpleGen().as_type("float64").as_type_auto_num(True)

    assert f.generate(test_df).dtype == "float64"
    assert f2.generate(test_df).dtype == "int8"


class TestSetFeature:

  def test_use_exist_value_if_cached_type(self):

    class RaiseGen(FeatureGen):

      def _gen(self, df: pd.DataFrame) -> pd.Series:
        raise Exception("This should not be called")

      def _feature_name(self) -> str:
        return "a"

    gen = RaiseGen()
    gen.set_feature(test_df)

  def test_handle_non_zero_origin_index(self):
    df = pd.DataFrame({"a": [1, 2, 3, 4, 5]}, index=[1, 2, 3, 4, 5])
    f = Features.many(a, a * 2, a.moving_average(2))

    result = f.set_features(df)

    assert result.index.equals(df.index)
    assert result["a"].equals(pd.Series([1, 2, 3, 4, 5], index=[1, 2, 3, 4, 5]))
    assert result["a_*_2"].equals(
        pd.Series([2, 4, 6, 8, 10], index=[1, 2, 3, 4, 5]))
    assert result["sma_2_of_a"].equals(
        pd.Series([np.nan, 1.5, 2.5, 3.5, 4.5], index=[1, 2, 3, 4, 5]))


class TestConAp:

  def test_return_self_with_features_by_callable(self):
    df = pd.DataFrame({"a": [1, 2, 3, 4, 5]})
    f = a.con_ap(lambda x: x.moving_sum(2))

    result = f.set_features(df)

    assert result.equals(
        pd.DataFrame({
            "a": [1, 2, 3, 4, 5],
            "sum_2_of_a": [np.nan, 3, 5, 7, 9]
        }))


class TestConAps:

  def test_return_self_with_features_by_callable(self):
    df = pd.DataFrame({"a": [1, 2, 3, 4, 5]})
    f = a.con_aps(lambda x: x.moving_sums([2, 3]))

    result = f.set_features(df)

    assert result.equals(
        pd.DataFrame({
            "a": [1, 2, 3, 4, 5],
            "sum_2_of_a": [np.nan, 3, 5, 7, 9],
            "sum_3_of_a": [np.nan, np.nan, 6, 9, 12]
        }))


class TestAsNameOf:

  def test_change_name(self):
    df = pd.DataFrame({"b": [1, 2, 3, 4, 5]})
    fs = a.as_name_of("b").to_features

    df = fs.set_features(df)

    assert fs.feature_names == ["b"]
    assert df.equals(pd.DataFrame({"b": [1, 2, 3, 4, 5]}))
