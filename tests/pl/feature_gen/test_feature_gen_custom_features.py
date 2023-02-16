import polars as pl
import declafe.pl.feature_gen as fg

df = pl.DataFrame({
    "a": [1, 2, 3, 4, 5],
    "b": [6, 7, 8, 9, 10],
    "c": [11, 12, 13, 14, 15],
    "d": [16, 17, 18, 19, 20],
})

a = fg.col("a")
b = fg.col("b")
c = fg.col("c")
d = fg.col("d")


def test_is_positive():
  f = (a - 3).is_positive()

  assert f(df).series_equal(
      pl.Series("(a_-_3)_is_positive", [False, False, False, True, True]))


def test_is_negative():
  f = (a - 3).is_negative()

  assert f(df).series_equal(
      pl.Series("(a_-_3)_is_negative", [True, True, False, False, False]))
