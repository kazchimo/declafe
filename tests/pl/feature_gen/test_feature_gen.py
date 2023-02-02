import polars as pl

from pl.feature_gen.feature_gen import FeatureGen, FailedToGenerate
import pytest


class AddFeature(FeatureGen):

  def __init__(self, left: str, right: str):
    super(AddFeature, self).__init__()
    self.left = left
    self.right = right

  def _gen(self, df: pl.DataFrame) -> pl.Series:
    return df[self.left] + df[self.right]

  def _feature_name(self) -> str:
    return f"{self.left} + {self.right}"


class TestCall:

  def test_call(self):
    df = pl.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    add = AddFeature("a", "b")
    assert (df["a"] + df["b"]).series_equal(add(df))


class TestGenerate:

  def test_generate(self):
    df = pl.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    add = AddFeature("a", "b")
    assert (df["a"] + df["b"]).series_equal(add.generate(df))

  def test_doesnt_generate_if_exists(self):

    class RaiseFeature(FeatureGen):

      def _gen(self, df: pl.DataFrame) -> pl.Series:
        raise Exception()

      def _feature_name(self) -> str:
        return "a"

    f = RaiseFeature()

    with pytest.raises(FailedToGenerate):
      f.generate(pl.DataFrame({"d": [1, 2, 3]}))

    df = pl.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    assert df["a"].series_equal(f.generate(df))


class TestFeatureName:

  def test_feature_name(self):
    f = AddFeature("a", "b")
    assert f.feature_name == "a + b"

  def test_override(self):
    f = AddFeature("a", "b").alias("c")
    assert f.feature_name == "c"


class TestAlias:

  def test_alias(self):
    f = AddFeature("a", "b").alias("c")
    assert f.feature_name == "c"


class TestAsNameOf:

  def test_as_name_of(self):
    f = AddFeature("a", "b").as_name_of("c")
    assert f.feature_name == "c"
