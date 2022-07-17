import pandas as pd

from declafe import Features
from declafe.feature_gen import FeatureGen
from declafe.feature_gen.binary import SARFeature
from declafe.feature_gen.dsl import c, col
from declafe.feature_gen.unary import LogFeature, SumFeature

test_df = pd.DataFrame({
    "a": list(range(1, 1001)),
    "b": list(range(1001, 2001))
})

a = col("a")
b = col("b")


class SimpleGen(FeatureGen):

  def gen(self, df: pd.DataFrame) -> pd.Series:
    return pd.Series(1, index=df.index)

  def _feature_name(self) -> str:
    return "test_gen"


_1 = c(1)


class Double(FeatureGen):

  def __init__(self, column: str):
    super().__init__()
    self.column = column

  def gen(self, df: pd.DataFrame) -> pd.Series:
    return df[self.column] * 2

  def _feature_name(self) -> str:
    return "double"


class TestFeatureName:

  def test_return_pre_defined_name_if_not_overrode(self):
    gen = SimpleGen()
    assert gen.feature_name == "test_gen"

  def test_return_overrode_name(self):
    gen = SimpleGen()
    gen.as_name_of("overrode")
    assert gen.feature_name == "overrode"


class TestLog:

  def test_return_log(self):
    assert _1.log().gen(test_df).equals(
        LogFeature("").gen_unary(pd.Series(1, index=test_df.index)))
    assert Double("a").log().gen(test_df).equals(
        LogFeature("").gen_unary(test_df["a"] * 2))


class TestMovingSums:

  def test_return_moving_sums(self):
    df1 = test_df.copy()
    df2 = test_df.copy()
    df1 = _1.set_feature(df1)
    df2 = _1.set_feature(df2)

    df1 = _1.moving_sums([3, 5]).set_features(df1)
    df2 = Features.many(SumFeature(3, _1.feature_name),
                        SumFeature(5, _1.feature_name)).set_features(df2)

    assert df1.equals(df2)


class TestSar:

  def test_return_sar(self):
    assert FeatureGen.sar("a", "b")\
      .gen(test_df)\
      .equals(SARFeature("a", "b").gen(test_df))


class TestAdd:

  def test_add(self):
    assert (a + 1).gen(test_df).equals(test_df["a"] + 1)
