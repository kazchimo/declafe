import polars as pl
import pl.feature_gen as fg


def test_accumulate():
  df = pl.DataFrame({"a": [1, 2, 3, 4, 5], "b": [4, 5, 6, 7, 8]})
  accumulate = fg.col("a").accumulate("add", lambda x, y: x + y)
  assert accumulate(df).series_equal(
      pl.Series(
          "accumulate_add(a)",
          [1, 3, 6, 10, 15],
      ))

  abs_accumulate = fg.col("a").abs().accumulate("add", lambda x, y: x + y)
  assert abs_accumulate(df).series_equal(
      pl.Series(
          "accumulate_add(|a|)",
          [1, 3, 6, 10, 15],
      ))
