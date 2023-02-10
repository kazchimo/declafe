import polars as pl
import declafe.pl.feature_gen as fg

a = fg.col("a")
b = fg.col("b")
c = fg.col("c")
d = fg.col("d")

df = pl.DataFrame({
    "a": [1, 2, 3, 4, 5],
    "b": [True, False, True, False, True],
    "c": [6, 7, 8, 9, 10],
    "d": ["a", "b", "c", "d", "e"],
})


def test_of_cond():
  f = fg.col("b").of_cond(fg.col("a"), fg.col("c"))
  assert f(df).series_equal(pl.Series("if_b_then_a_else_c", [1, 7, 3, 9, 5]))

  f = ((a % 2) == 0).of_cond(c, d)
  assert f(df).series_equal(
      pl.Series("if_((a_%_2)_==_0)_then_c_else_d", ["a", "7", "c", "9", "e"]))


def test_cond():
  f = fg.cond(fg.col("b"), fg.col("a"), fg.col("c"))
  assert f(df).series_equal(pl.Series("if_b_then_a_else_c", [1, 7, 3, 9, 5]))

  f = fg.cond((a % 2) == 0, c, d)
  assert f(df).series_equal(
      pl.Series("if_((a_%_2)_==_0)_then_c_else_d", ["a", "7", "c", "9", "e"]))
