import polars as pl

from pl.feature_gen.feature_gen import FeatureGen
import pl.feature_gen as fg


class AddFeature(FeatureGen):

  def __init__(self, left: str, right: str):
    super(AddFeature, self).__init__()
    self.left = left
    self.right = right

  def _expr(self) -> pl.Expr:
    return pl.col(self.left) + pl.col(self.right)

  def _feature_name(self) -> str:
    return f"{self.left} + {self.right}"


class TestCall:

  def test_call(self):
    df = pl.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    add = AddFeature("a", "b")
    assert (df["a"] + df["b"]).alias("a + b").series_equal(add(df))


class TestGenerate:

  def test_generate(self):
    df = pl.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    add = AddFeature("a", "b")
    assert (df["a"] + df["b"]).alias("a + b").series_equal(add.generate(df))


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


class Test_WrappedFeatureName:

  def test_wrapped_feature_name(self):
    assert fg.col("a").wrapped_feature_name == "a"
    assert fg.lit(1).wrapped_feature_name == "1"
    assert fg.col("a").abs().wrapped_feature_name == "(|a|)"
    assert fg.col("a").abs().log().wrapped_feature_name == "(log(|a|))"
