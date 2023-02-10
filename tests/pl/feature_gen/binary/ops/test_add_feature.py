import polars as pl
import declafe.pl.feature_gen as fg


def test_add_feature():
  df = pl.DataFrame({"a": [1, 2, 3, 4, 5, 6], "b": [1, 2, -3, 4, 5, 6]})

  add = fg.col("a") + fg.col("b")
  assert add(df).series_equal(pl.Series(
      "a_+_b",
      [2, 4, 0, 8, 10, 12],
  ))

  abs_add = fg.col("b").abs() + fg.col("a")
  assert abs_add(df).series_equal(pl.Series(
      "(|b|)_+_a",
      [2, 4, 6, 8, 10, 12],
  ))

  add_const = fg.col("a") + 1
  assert add_const(df).series_equal(pl.Series(
      "a_+_1",
      [2, 3, 4, 5, 6, 7],
  ))

  add_lit = fg.col("a") + fg.lit(1)
  assert add_lit(df).series_equal(pl.Series(
      "a_+_1",
      [2, 3, 4, 5, 6, 7],
  ))


def test_radd_feature():
  df = pl.DataFrame({"a": [1, 2, 3, 4, 5, 6], "b": [1, 2, -3, 4, 5, 6]})

  radd = 1 + fg.col("a")
  assert radd(df).series_equal(pl.Series(
      "1_+_a",
      [2, 3, 4, 5, 6, 7],
  ))

  abs_radd = 1 + fg.col("b").abs()
  assert abs_radd(df).series_equal(pl.Series(
      "1_+_(|b|)",
      [2, 3, 4, 5, 6, 7],
  ))

  radd_const = fg.lit(1) + fg.col("a")
  assert radd_const(df).series_equal(pl.Series(
      "1_+_a",
      [2, 3, 4, 5, 6, 7],
  ))
