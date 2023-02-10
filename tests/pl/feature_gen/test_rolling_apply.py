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


def test_rolling_apply():
  f = a.rolling_apply(3, lambda x: sum(x), "sum")
  assert f(df).series_equal(
      pl.Series("rolling_apply_sum_over_a_3", [None, None, 6, 9, 12]))

  f = (a + c).rolling_apply(3, lambda x: sum(x), "sum")
  assert f(df).series_equal(
      pl.Series("rolling_apply_sum_over_(a_+_c)_3", [None, None, 27, 33, 39]))
