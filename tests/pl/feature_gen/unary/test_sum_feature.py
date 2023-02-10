import polars as pl
import pl.feature_gen as fg


def test_rolling_sum_feature():
  df = pl.DataFrame({"a": [1, 2, 3, 4, 5], "b": [4, 5, 6, 7, 8]})
  sum = fg.col("a").rolling_sum(2)
  assert sum(df).series_equal(pl.Series(
      "rolling_sum2(a)",
      [None, 3, 5, 7, 9],
  ))


def test_sum_feature():
  df = pl.DataFrame({"a": [1, 2, 3, 4, 5], "b": [4, 5, 6, 7, 8]})
  sum = fg.col("a").sum(2)
  assert sum(df).series_equal(pl.Series(
      "rolling_sum2(a)",
      [None, 3, 5, 7, 9],
  ))
