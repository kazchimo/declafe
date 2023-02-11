import polars as pl
import declafe.pl.feature_gen as fg
import numpy as np


def test_fill_nan():
  df = pl.DataFrame({
      "a": [np.nan, 2, 3, 4, 5, 6],
      "b": [np.nan, 2, -3, 4, 5, 6]
  })

  fill_null = fg.col("a").fill_nan(0)
  assert fill_null(df).series_equal(
      pl.Series(
          "fill_nan(a, 0)",
          [0, 2, 3, 4, 5, 6],
      ))

  fill_null = fg.col("b").abs().fill_nan(99)
  assert fill_null(df).series_equal(
      pl.Series(
          "fill_nan(|b|, 99)",
          [99, 2, 3, 4, 5, 6],
      ))
