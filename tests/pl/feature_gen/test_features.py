import polars as pl

from pl.feature_gen.feature_gen import FeatureGen
from pl.feature_gen.features import Features
import pl.feature_gen.constructor_dsl as dsl


class AddFeature(FeatureGen):

  def __init__(self, left: str, right: str):
    super(AddFeature, self).__init__()
    self.left = left
    self.right = right

  def _expr(self) -> pl.Expr:
    return pl.col(self.left) + pl.col(self.right)

  def _feature_name(self) -> str:
    return f"{self.left} + {self.right}"


class SubFeature(FeatureGen):

  def __init__(self, left: str, right: str):
    super(SubFeature, self).__init__()
    self.left = left
    self.right = right

  def _expr(self) -> pl.Expr:
    return pl.col(self.left) - pl.col(self.right)

  def _feature_name(self) -> str:
    return f"{self.left} - {self.right}"


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
