import polars as pl
import declafe.pl.feature_gen as fg


def test_log_feature():
  df = pl.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
  log = fg.col("a").log()
  assert df["a"].log().alias("log(a)").series_equal(log(df))

  abs_log = fg.col("a").abs().log()
  assert df["a"].abs().log().alias("log(|a|)").series_equal(abs_log(df))
