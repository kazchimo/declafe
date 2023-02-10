import polars as pl
import declafe.pl.feature_gen as fg


def test_rolling_std_feature():
  df = pl.DataFrame({"a": [1, 2, 3, 4, 5], "b": [4, 5, 6, 7, 8]})
  rolling_std = fg.col("a").rolling_std(2).round_n(2)
  assert rolling_std(df).series_equal(
      pl.Series(
          "round2(rolling_std2(a))",
          [None, 0.71, 0.71, 0.71, 0.71],
      ))


def test_std():
  df = pl.DataFrame({"a": [1, 2, 3, 4, 5], "b": [4, 5, 6, 7, 8]})
  rolling_std = fg.col("a").std(2).round_n(2)
  assert rolling_std(df).series_equal(
      pl.Series(
          "round2(rolling_std2(a))",
          [None, 0.71, 0.71, 0.71, 0.71],
      ))
