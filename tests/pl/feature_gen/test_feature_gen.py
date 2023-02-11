import polars as pl

from declafe.pl.feature_gen.feature_gen import FeatureGen
import declafe.pl.feature_gen as fg
from declafe.pl.feature_gen.features import Features


class AddFeature(FeatureGen):

  def __init__(self, left: str, right: str):
    super(AddFeature, self).__init__()
    self.left = left
    self.right = right
    self.change_seperator(" ")

  def _expr(self) -> pl.Expr:
    return pl.col(self.left) + pl.col(self.right)

  def _feature_names(self) -> list[str]:
    return [f"{self.left}", "+", f"{self.right}"]


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


class TestMapAlias:

  def test_map_alias(self):
    f = ((fg.col("a") + fg.col("b")) *
         2).map_alias(lambda s: s.replace("_", "="))
    assert f.feature_name == "(a=+=b)=*=2"


class TestAsNameOf:

  def test_as_name_of(self):
    f = AddFeature("a", "b").as_name_of("c")
    assert f.feature_name == "c"


class TestExtract:

  def test_extract(self):
    df = pl.DataFrame({"a + b": [1, 2, 3]})
    f = AddFeature("a", "b")
    assert f.extract(df).series_equal(df["a + b"])


class TestTransform:

  def test_transform(self):
    df = pl.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    f = AddFeature("a", "b")
    assert f.transform(df).frame_equal(
        df.with_columns((pl.col("a") + pl.col("b")).alias("a + b")))

  def test_set_feature(self):
    df = pl.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    f = AddFeature("a", "b")
    assert f.set_feature(df).frame_equal(
        df.with_columns((pl.col("a") + pl.col("b")).alias("a + b")))


class TestToFeatures:

  def test_to_features(self):
    f = AddFeature("a", "b")
    assert f.to_features == Features.one(f)


class TestCombine:

  def test_combine(self):
    f = AddFeature("a", "b")
    ff = AddFeature("c", "d")
    assert f.combine(ff) == Features.many(f, ff)


class TestConApp:

  def test_con_app(self):
    df = pl.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    f = fg.col("a").con_ap(lambda x: x + 1)
    res = f(df)
    assert res["a_+_1"].series_equal(pl.Series("a_+_1", [2, 3, 4]))
    assert res["a"].series_equal(pl.Series("a", [1, 2, 3]))


class TestConAps:

  def test_con_aps(self):
    df = pl.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    f = fg.col("a").con_aps(lambda x: Features.many(x + 1, x + 2))
    res = f(df)

    assert res["a_+_1"].series_equal(pl.Series("a_+_1", [2, 3, 4]))
    assert res["a_+_2"].series_equal(pl.Series("a_+_2", [3, 4, 5]))
    assert res["a"].series_equal(pl.Series("a", [1, 2, 3]))


class TestStr:

  def test_str(self):
    f = AddFeature("a", "b")
    assert str(f) == "a + b"


class Test_WrappedFeatureName:

  def test_wrapped_feature_name(self):
    assert fg.col("a").wrapped_feature_name == "a"
    assert fg.lit(1).wrapped_feature_name == "1"
    assert fg.col("a").abs().wrapped_feature_name == "(|a|)"
    assert fg.col("a").abs().log().wrapped_feature_name == "(log(|a|))"


class TestChangeSeperator:

  def test_change_seperator(self):
    f = fg.col("a").log().replace(2, 10)

    assert f.feature_name == "replace_2_of_(log(a))_to_10"
    assert f.change_seperator(" ").feature_name == "replace 2 of (log(a)) to 10"
