import polars as pl
import pl.feature_gen as fg


def test_sub_feature():
  df = pl.DataFrame({"a": [1, 2, 3, 4, 5, 6], "b": [1, 2, -3, 4, 5, 6]})

  sub = fg.col("a") - fg.col("b")
  assert sub(df).series_equal(pl.Series(
      "a_-_b",
      [0, 0, 6, 0, 0, 0],
  ))

  abs_sub = fg.col("b").abs() - fg.col("a")
  assert abs_sub(df).series_equal(pl.Series(
      "(|b|)_-_a",
      [0, 0, 0, 0, 0, 0],
  ))

  sub_const = fg.col("a") - 1
  assert sub_const(df).series_equal(pl.Series(
      "a_-_1",
      [0, 1, 2, 3, 4, 5],
  ))

  sub_lit = fg.col("a") - fg.lit(1)
  assert sub_lit(df).series_equal(pl.Series(
      "a_-_1",
      [0, 1, 2, 3, 4, 5],
  ))


def test_rsub_feature():
  df = pl.DataFrame({"a": [1, 2, 3, 4, 5, 6], "b": [1, 2, -3, 4, 5, 6]})

  rsub = 1 - fg.col("a")
  assert rsub(df).series_equal(pl.Series(
      "1_-_a",
      [0, -1, -2, -3, -4, -5],
  ))

  abs_rsub = 1 - fg.col("b").abs()
  assert abs_rsub(df).series_equal(
      pl.Series(
          "1_-_(|b|)",
          [0, -1, -2, -3, -4, -5],
      ))

  rsub_const = fg.lit(1) - fg.col("a")
  assert rsub_const(df).series_equal(
      pl.Series(
          "1_-_a",
          [0, -1, -2, -3, -4, -5],
      ))
