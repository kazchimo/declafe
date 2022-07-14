import pandas as pd

from declafe import FeatureGen, LogFeature
from declafe.dsl import c

test_df = pd.DataFrame(
    {
        "a": list(range(1, 1001)),
        "b": list(range(1001, 2001))
    })


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
