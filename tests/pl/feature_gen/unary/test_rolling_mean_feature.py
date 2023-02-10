import polars as pl
import declafe.pl.feature_gen as fg


def test_rolling_mean_feature():
  df = pl.DataFrame({"a": [1, 2, 3, 4, 5], "b": [4, 5, 6, 7, 8]})
  rolling_mean = fg.col("a").rolling_mean(2)
  assert rolling_mean(df).series_equal(
      pl.Series(
          "rolling_mean2(a)",
          [None, 1.5, 2.5, 3.5, 4.5],
      ))


def test_mean():
  df = pl.DataFrame({"a": [1, 2, 3, 4, 5], "b": [4, 5, 6, 7, 8]})
  rolling_mean = fg.col("a").mean(2)
  assert rolling_mean(df).series_equal(
      pl.Series(
          "rolling_mean2(a)",
          [None, 1.5, 2.5, 3.5, 4.5],
      ))
