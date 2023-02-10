import polars as pl

from pl.feature_gen.feature_gen import FeatureGen
from pl.feature_gen.features import Features
import pl.feature_gen.constructor_dsl as dsl
import pl.feature_gen as fg
from pl.feature_gen.unary.id_feature import IdFeature

a = fg.col("a")
b = fg.col("b")


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


class SubFeature(FeatureGen):

  def __init__(self, left: str, right: str):
    super(SubFeature, self).__init__()
    self.left = left
    self.right = right
    self.change_seperator(" ")

  def _expr(self) -> pl.Expr:
    return pl.col(self.left) - pl.col(self.right)

  def _feature_names(self) -> list[str]:
    return [f"{self.left}", "-", f"{self.right}"]


class TestInit:

  def test_exclude_dup(self):
    df = pl.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    add = AddFeature("a", "b")
    sub = SubFeature("a", "b")
    fs = Features([add, sub, add])
    result = fs(df)

    assert result.frame_equal(
        pl.DataFrame({
            "a": [1, 2, 3],
            "b": [4, 5, 6],
            "a + b": [5, 7, 9],
            "a - b": [-3, -3, -3],
        }))


class TestTransform:

  def test_gen_features_in_addition_to_origs(self):
    df = pl.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    add = AddFeature("a", "b")
    sub = SubFeature("a", "b")
    fs = Features([add, sub])
    result = fs(df)

    assert result.frame_equal(
        pl.DataFrame({
            "a": [1, 2, 3],
            "b": [4, 5, 6],
            "a + b": [5, 7, 9],
            "a - b": [-3, -3, -3],
        }))

  def test_set_features(self):
    df = pl.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    add = AddFeature("a", "b")
    sub = SubFeature("a", "b")
    fs = Features([add, sub])
    result = fs(df)

    assert result.frame_equal(
        pl.DataFrame({
            "a": [1, 2, 3],
            "b": [4, 5, 6],
            "a + b": [5, 7, 9],
            "a - b": [-3, -3, -3],
        }))

  def test_call(self):
    df = pl.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    add = AddFeature("a", "b")
    sub = SubFeature("a", "b")
    fs = Features([add, sub])
    result = fs(df)

    assert result.frame_equal(
        pl.DataFrame({
            "a": [1, 2, 3],
            "b": [4, 5, 6],
            "a + b": [5, 7, 9],
            "a - b": [-3, -3, -3],
        }))


class TestFeatureNames:

  def test_return_feature_names(self):
    add = AddFeature("a", "b")
    sub = SubFeature("a", "b")
    fs = dsl.features(add, sub)
    assert fs.feature_names == ["a + b", "a - b"]


class TestContains:

  def test_contains(self):
    add = AddFeature("a", "b")
    sub = SubFeature("a", "b")
    fs = dsl.features(add, sub)
    assert fs.contains(add)
    assert fs.contains(sub)
    assert not fs.contains(AddFeature("a", "c"))

  def test_ops(self):
    add = AddFeature("a", "b")
    sub = SubFeature("a", "b")
    fs = dsl.features(add, sub)
    assert add in fs
    assert sub in fs
    assert AddFeature("a", "c") not in fs


class TestMap:

  def test_map(self):
    df = pl.DataFrame({"a": [1, -2, 3], "b": [4, -5, 6]})
    fs = fg.features(fg.col("a"), fg.col("b")).map(lambda x: x.abs())

    print(fs(df))

    assert fs(df).frame_equal(
        pl.DataFrame({
            "a": [1, -2, 3],
            "b": [4, -5, 6],
            "|a|": [1, 2, 3],
            "|b|": [4, 5, 6],
        }))


class TestFlatMap:

  def test_flat_map(self):
    df = pl.DataFrame({"a": [1, -2, 3], "b": [4, -5, 6]})
    fs = fg.features(fg.col("a"),
                     fg.col("b")).flat_map(lambda x: [x.abs(), x + 1])

    assert fs(df).frame_equal(
        pl.DataFrame({
            "a": [1, -2, 3],
            "b": [4, -5, 6],
            "|a|": [1, 2, 3],
            "a_+_1": [2, -1, 4],
            "|b|": [4, 5, 6],
            "b_+_1": [5, -4, 7],
        }))

  def test_flat_map_with_features(self):
    df = pl.DataFrame({"a": [1, -2, 3], "b": [4, -5, 6]})
    fs = fg.features(
        fg.col("a"),
        fg.col("b")).flat_map(lambda x: fg.features(x.abs(), x + 1))

    assert fs(df).frame_equal(
        pl.DataFrame({
            "a": [1, -2, 3],
            "b": [4, -5, 6],
            "|a|": [1, 2, 3],
            "a_+_1": [2, -1, 4],
            "|b|": [4, 5, 6],
            "b_+_1": [5, -4, 7],
        }))


class TestFeatureCount:

  def test_feature_count(self):
    fs = fg.features(fg.col("a"), fg.col("b")).map(lambda x: x.abs())

    assert fs.feature_count == 2


class TestExtract:

  def test_extract(self):
    df = pl.DataFrame({"a": [1, -2, 3], "b": [4, -5, 6]})
    fs = fg.features(a, b).map(lambda x: x.abs())
    result = fs.extract(fs(df))
    assert result.frame_equal(
        pl.DataFrame({
            "|a|": [1, 2, 3],
            "|b|": [4, 5, 6],
        }))


class TestAddFeature:

  def test_add_feature(self):
    df = pl.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    fs = fg.col("a").to_features
    fs = fs.add_feature(fg.col("b"))

    res = fs(df)
    assert res["a"].series_equal(df["a"])
    assert res["b"].series_equal(df["b"])


class TestAddFeatures:

  def test_add_features(self):
    df = pl.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    fs = fg.col("a").to_features
    fs = fs.add_features([fg.col("b"), fg.col("a") + fg.col("b")])

    res = fs(df)
    assert res["a"].series_equal(df["a"])
    assert res["b"].series_equal(df["b"])
    assert res["a_+_b"].series_equal((df["a"] + df["b"]).alias("a_+_b"))

  def test_add_features_with_features(self):
    df = pl.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    fs = fg.col("a").to_features
    fs = fs.add_features(Features.many(fg.col("b"), fg.col("a") + fg.col("b")))

    res = fs(df)
    assert res["a"].series_equal(df["a"])
    assert res["b"].series_equal(df["b"])
    assert res["a_+_b"].series_equal((df["a"] + df["b"]).alias("a_+_b"))


class TestFilterByName:

  def test_filter_by_name(self):
    df = pl.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    fs = Features.many(a, b, a + b).filter_by_name(["a", "a_+_b"])

    res = fs(df)
    assert res["a"].series_equal(df["a"])
    assert res["a_+_b"].series_equal((df["a"] + df["b"]).alias("a_+_b"))
    assert "b" not in fs

  def test_filter_not_by_name(self):
    df = pl.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    fs = Features.many(a, b, a + b).filter_not_by_name(["a", "a_+_b"])

    res = fs(df)
    assert res["b"].series_equal(df["b"])
    assert "a" not in fs
    assert "a_+_b" not in fs


class TestFilter:

  def test_filter(self):
    df = pl.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    fs = Features.many(a, b, a + b).filter(lambda f: f.feature_name == "a")

    res = fs(df)
    assert res["a"].series_equal(df["a"])
    assert "b" not in fs
    assert "a_+_b" not in fs

  def test_filter_not(self):
    df = pl.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    fs = Features.many(a, b, a + b).filter_not(lambda f: f.feature_name == "a")

    res = fs(df)
    assert res["b"].series_equal(df["b"])
    assert res["a_+_b"].series_equal((df["a"] + df["b"]).alias("a_+_b"))
    assert "a" not in fs


class TestFilterByGen:

  def test_filter_by_gen(self):
    df = pl.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    fs = Features.many(a, b, a + b).filter_by_gen(IdFeature)

    res = fs(df)
    assert res["a"].series_equal(df["a"])
    assert res["b"].series_equal(df["b"])
    assert "a_+_b" not in fs

  def test_filter_not_by_gen(self):
    df = pl.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    fs = Features.many(a, b, a + b).filter_not_by_gen(IdFeature)

    res = fs(df)
    assert res["a_+_b"].series_equal((df["a"] + df["b"]).alias("a_+_b"))
    assert "a" not in fs
    assert "b" not in fs


class TestZipWith:

  def test_zip_with(self):
    df = pl.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    fs1 = fg.features(a, b)
    fs2 = fs1.map(lambda x: x + 2)
    fs = fs1.zip_with(fs2, lambda x, y: x * y)

    assert fs(df).frame_equal(
        pl.DataFrame({
            "a": [1, 2, 3],
            "b": [4, 5, 6],
            "a_*_(a_+_2)": [3, 8, 15],
            "b_*_(b_+_2)": [24, 35, 48],
        }))


class TestReduce:

  def test_reduce(self):
    df = pl.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    fs = fg.features(a, b).reduce(lambda x, y: x + y, fg.lit(1))

    assert fs(df).series_equal((df["a"] + df["b"] + 1).alias("(1_+_a)_+_b"))

  def test_reduce_with_value(self):
    df = pl.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    fs = fg.features(a, b).reduce(lambda x, y: x + y, 1)

    assert fs(df).series_equal((df["a"] + df["b"] + 1).alias("(1_+_a)_+_b"))


class TestAdd:

  def test_add(self):
    df = pl.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    fs = fg.features(a, b).map(lambda x: x + 2) + fg.features(
        a, b).map(lambda x: x * 2)

    assert fs(df).frame_equal(
        pl.DataFrame({
            "a": [1, 2, 3],
            "b": [4, 5, 6],
            "a_+_2": [3, 4, 5],
            "b_+_2": [6, 7, 8],
            "a_*_2": [2, 4, 6],
            "b_*_2": [8, 10, 12],
        }))


class TestEq:

  def test_eq(self):
    fs1 = fg.features(a, b).map(lambda x: x + 2)
    fs2 = fg.features(a + 2, b + 2)

    assert fs1 == fs2


class TestLen:

  def test_len(self):
    fs = fg.features(a, b).map(lambda x: x + 2)
    assert len(fs) == 2


class TestIter:

  def test_iter(self):
    df = pl.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    fs = fg.features(a, b).map(lambda x: x + 2)
    fs = Features([f / 2 for f in fs])

    assert fs(df).frame_equal(
        pl.DataFrame({
            "a": [1, 2, 3],
            "b": [4, 5, 6],
            "(a_+_2)_/_2": [1.5, 2, 2.5],
            "(b_+_2)_/_2": [3, 3.5, 4],
        }))


class TestConstructor:

  def test_empty(self):
    assert Features.empty() == Features([])

  def test_one(self):
    assert Features.one(a) == Features([a])

  def test_many(self):
    assert Features.many(a, b) == Features([a, b])

  def test_iter_over(self):
    df = pl.DataFrame({"a": [3, 2, 3], "b": [4, 5, 6]})
    fs = Features.iter_over([1, 2])(a.max)

    print(fs(df))
    assert fs(df).frame_equal(
        pl.DataFrame({
            "a": [3, 2, 3],
            "b": [4, 5, 6],
            "rolling_max1(a)": [3, 2, 3],
            "rolling_max2(a)": [None, 3, 3],
        }))
