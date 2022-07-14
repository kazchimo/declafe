import pandas as pd

from declafe import FeatureGen


class TestFeatureName:

  class SimpleGen(FeatureGen):

    def gen(self, df: pd.DataFrame) -> pd.Series:
      return pd.Series("test", index=df.index)

    def _feature_name(self) -> str:
      return "test_gen"

  def test_return_pre_defined_name_if_not_overrode(self):
    gen = self.SimpleGen()
    assert gen.feature_name == "test_gen"

  def test_return_overrode_name(self):
    gen = self.SimpleGen()
    gen.as_name_of("overrode")
    assert gen.feature_name == "overrode"
