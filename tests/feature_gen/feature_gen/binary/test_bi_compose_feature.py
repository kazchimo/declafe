import pandas as pd

from declafe import col
from declafe.feature_gen.binary import BiComposeFeature, AddFeature

a = col("a")
b = col("b")


class TestGen:
  def test_return_composed_feature(self):
    df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
    gen = BiComposeFeature(a * 2, b * 3, AddFeature)

    assert gen.generate(df).equals(pd.Series([14, 19, 24]))

class TestFeatureName:
  def test_return_composed_feature_name(self):
    gen = BiComposeFeature(a * 2, b * 3, AddFeature)

    assert gen.feature_name == "(a_*_2)_+_(b_*_3)"
