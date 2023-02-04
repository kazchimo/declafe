import polars as pl
import pl.feature_gen as fg


def test_rolling_max_feature():
  df = pl.DataFrame({"a": [1, 2, 3, 4, 5], "b": [4, 5, 6, 7, 8]})
  rolling_max = fg.col("a").rolling_max(2)
  assert rolling_max(df).series_equal(
      pl.Series(
          "rolling_max2(a)",
          [None, 2, 3, 4, 5],
      ))


def test_max():
  df = pl.DataFrame({"a": [1, 2, 3, 4, 5], "b": [4, 5, 6, 7, 8]})
  rolling_max = fg.col("a").max(2)
  assert rolling_max(df).series_equal(
      pl.Series(
          "rolling_max2(a)",
          [None, 2, 3, 4, 5],
      ))
