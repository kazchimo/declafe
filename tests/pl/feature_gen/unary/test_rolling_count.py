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
    "d": ["a", "b", "a", "a", "c"],
})


def test_rolling_count():
  f = b.rolling_count(3, True)
  assert f(df).series_equal(
      pl.Series("rolling_count_True_over_b_3", [None, None, 2, 1, 2]))

  f = (a + c).rolling_count(3, 9)
  assert f(df).series_equal(
      pl.Series("rolling_count_9_over_(a_+_c)_3", [None, None, 1, 1, 0]))

  f = d.rolling_count(3, "a")
  assert f(df).series_equal(
      pl.Series("rolling_count_a_over_d_3", [None, None, 2, 2, 2]))


def test_rolling_true_count():
  f = b.rolling_true_count(3)
  assert f(df).series_equal(
      pl.Series("rolling_count_True_over_b_3", [None, None, 2, 1, 2]))


def test_rolling_false_count():
  f = b.rolling_false_count(3)
  assert f(df).series_equal(
      pl.Series("rolling_count_False_over_b_3", [None, None, 1, 2, 1]))
