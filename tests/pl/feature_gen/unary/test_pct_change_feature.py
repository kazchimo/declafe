import polars as pl
import pl.feature_gen as fg


def test_pct_change_feature():
  df = pl.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
  pct_change = fg.col("a").pct_change(1)

  assert df["a"].pct_change().alias("pct_change1(a)")\
    .series_equal(pct_change(df))
