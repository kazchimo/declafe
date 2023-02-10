import polars as pl
import declafe.pl.feature_gen as fg


def test_maximum_feature():
  df = pl.DataFrame({"a": [1, 2, 3, 4, 5], "b": [4, 5, 6, 7, 8]})
  maximum = fg.col("a").maximum(2)
  assert maximum(df).series_equal(pl.Series(
      "maximum(a, 2)",
      [2, 2, 3, 4, 5],
  ))
