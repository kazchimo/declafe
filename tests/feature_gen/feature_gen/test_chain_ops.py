import numpy as np
import pandas as pd
import talib

from declafe import col, c, FeatureGen, Features
from declafe.feature_gen.binary import SARFeature
from declafe.feature_gen.unary import LogFeature, SumFeature

test_df = pd.DataFrame({
    "a": list(range(1, 1001)),
    "b": list(range(1001, 2001))
})

a = col("a")
b = col("b")
_1 = c(1)

class TestMinComp:
  def test_return_min_value(self):
    df = test_df.copy()
    result = a.min_comp(500).gen(df)
    pred = pd.Series(list(range(1, 501)) + [500] * 500)

    assert result.equals(pred)


class TestMaxComp:
  def test_return_max_value(self):
    df = test_df.copy()
    result = a.max_comp(500).gen(df)
    pred = pd.Series([500] * 500 + list(range(501, 1001)))

    assert result.equals(pred)

class Double(FeatureGen):

  def __init__(self, column: str):
    super().__init__()
    self.column = column

  def gen(self, df: pd.DataFrame) -> pd.Series:
    return df[self.column] * 2

  def _feature_name(self) -> str:
    return "double"

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
    assert FeatureGen.sar("a", "b") \
      .gen(test_df) \
      .equals(SARFeature("a", "b").gen(test_df))


class TestAdd:

  def test_add(self):
    assert (a + 1).gen(test_df).equals(test_df["a"] + 1)

class TestApo:
  def test_calc_apo(self):
    assert a.apo(12, 26).gen(test_df).equals(talib.APO(test_df["a"], 12, 26))

class TestInvert:
  def test_invert(self):
    assert (~a).gen(pd.DataFrame({"a": [True, False]})).equals(pd.Series([False, True]))

class TestLag:
  def test_lag(self):
    assert a.lag(1).gen(test_df).equals(test_df["a"].shift(1))

class TestReplace:
  def test_replace(self):
    gen = a.lag(1).replace(np.nan, 99999)
    assert list(gen.gen(test_df)) == [99999] + list(range(1, 1000))

class TestReplaceNa:
  def test_replace_na(self):
    gen = a.lag(1).replace_na(99999)
    assert list(gen.gen(test_df)) == [99999] + list(range(1, 1000))
