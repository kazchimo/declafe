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

  def gen(self, df: pd.DataFrame) -> pd.Series:
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
    fs = Features([SimpleGen(), ConstFeature(1), ConstFeature(2).as_name_of("test_gen")])

    assert fs.feature_count == 2
    assert fs.feature_names == ["test_gen", "1"]
