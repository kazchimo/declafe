import polars as pl

from pl.feature_gen.unary.unary_feature import UnaryFeature
import pl.feature_gen as fg


class Plus1Feature(UnaryFeature):

  def _unary_expr(self, orig_col: pl.Expr):
    return orig_col + 1

  def _feature_name(self) -> str:
    return f"{self._col_wrapped_feature_name} + 1"


class TestUnaryFeature:

  def test_with_str(self):
    df = pl.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    plus1 = Plus1Feature("a")
    assert pl.Series("a + 1", [2, 3, 4]).series_equal(plus1(df))

  def test_with_col(self):
    df = pl.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    plus1 = Plus1Feature(fg.col("a"))
    assert pl.Series("a + 1", [2, 3, 4]).series_equal(plus1(df))

  def test_chain(self):
    df = pl.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    plus1 = Plus1Feature(fg.col("a"))
    plus2 = Plus1Feature(plus1)
    print(plus2(df))
    assert pl.Series("(a + 1) + 1", [3, 4, 5]).series_equal(plus2(df))

  def test_col_feature(self):
    plus1 = Plus1Feature(fg.col("a"))

    assert plus1.col_feature.equals(fg.col("a"))
