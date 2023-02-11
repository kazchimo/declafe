import polars as pl
import declafe.pl.feature_gen as fg


def test_fill_null():
  df = pl.DataFrame({"a": [1, 2, 3, 4, 5, 6], "b": [1, 2, -3, 4, 5, 6]})

  fill_null = fg.col("a").lag(1).fill_null(0)
  assert fill_null(df).series_equal(
      pl.Series(
          "fill_null(lag1(a), 0)",
          [0, 1, 2, 3, 4, 5],
      ))

  fill_null = fg.col("b").abs().lag(1).fill_null(99)
  assert fill_null(df).series_equal(
      pl.Series(
          "fill_null(lag1(|b|), 99)",
          [99, 1, 2, 3, 4, 5],
      ))

  zero_fill_null = fg.col("b").abs().lag(1).fill_null(storategy="zero")
  assert zero_fill_null(df).series_equal(
      pl.Series(
          "zero_fill_null(lag1(|b|))",
          [0, 1, 2, 3, 4, 5],
      ))
