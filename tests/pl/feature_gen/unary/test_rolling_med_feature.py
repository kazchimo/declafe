import polars as pl
import pl.feature_gen as fg


def test_rolling_med_feature():
  df = pl.DataFrame({"a": [1, 2, 3, 4, 5], "b": [4, 5, 6, 7, 8]})
  rolling_med = fg.col("a").rolling_median(2)
  assert rolling_med(df).series_equal(
      pl.Series(
          "rolling_med2(a)",
          [None, 1.5, 2.5, 3.5, 4.5],
      ))


def test_median():
  df = pl.DataFrame({"a": [1, 2, 3, 4, 5], "b": [4, 5, 6, 7, 8]})
  rolling_med = fg.col("a").median(2)
  assert rolling_med(df).series_equal(
      pl.Series(
          "rolling_med2(a)",
          [None, 1.5, 2.5, 3.5, 4.5],
      ))


def test_med():
  df = pl.DataFrame({"a": [1, 2, 3, 4, 5], "b": [4, 5, 6, 7, 8]})
  rolling_med = fg.col("a").med(2)
  assert rolling_med(df).series_equal(
      pl.Series(
          "rolling_med2(a)",
          [None, 1.5, 2.5, 3.5, 4.5],
      ))
