import polars as pl
import pl.feature_gen as fg


def test_rolling_min_feature():
  df = pl.DataFrame({"a": [1, 2, 3, 4, 5], "b": [4, 5, 6, 7, 8]})
  rolling_min = fg.col("a").rolling_min(2)
  assert rolling_min(df).series_equal(
      pl.Series(
          "rolling_min2(a)",
          [None, 1, 2, 3, 4],
      ))


def test_min():
  df = pl.DataFrame({"a": [1, 2, 3, 4, 5], "b": [4, 5, 6, 7, 8]})
  rolling_min = fg.col("a").min(2)
  assert rolling_min(df).series_equal(
      pl.Series(
          "rolling_min2(a)",
          [None, 1, 2, 3, 4],
      ))
