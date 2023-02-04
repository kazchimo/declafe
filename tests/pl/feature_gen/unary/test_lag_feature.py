import polars as pl
import pl.feature_gen as fg


def test_lag_feature():
  df = pl.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
  lag = fg.col("a").lag(1)
  assert df["a"].shift(1).alias("lag_1_of_a").series_equal(lag(df))


def test_shift_feature():
  df = pl.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
  shift = fg.col("a").shift(1)
  assert df["a"].shift(1).alias("lag_1_of_a").series_equal(shift(df))
