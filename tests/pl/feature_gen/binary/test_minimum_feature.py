import polars as pl
import declafe.pl.feature_gen as fg


def test_minimum_feature():
  df = pl.DataFrame({"a": [1, 2, 3, 4, 5], "b": [4, 5, 6, 7, 8]})
  minimum = fg.col("a").minimum(2)
  assert minimum(df).series_equal(pl.Series(
      "minimum(a, 2)",
      [1, 2, 2, 2, 2],
  ))

  minimum = fg.col("a").minimum(fg.col("b"))
  assert minimum(df).series_equal(pl.Series(
      "minimum(a, b)",
      [1, 2, 3, 4, 5],
  ))
