import polars as pl
import declafe.pl.feature_gen as fg


def test_replace_feature():
  df = pl.DataFrame({"a": [1, 2, 3, 4, 5], "b": [4, 5, 6, 7, 8]})
  replace = fg.col("a").replace(2, 10)
  assert replace(df).series_equal(
      pl.Series(
          "replace_2_of_a_to_10",
          [1, 10, 3, 4, 5],
      ))
