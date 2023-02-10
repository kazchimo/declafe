import polars as pl
import declafe.pl.feature_gen as fg


def test_exists_within_feature():
  df = pl.DataFrame({"a": [1, 2, 3, 4, 5, 6], "b": [1, 2, -3, 4, 5, 6]})
  exists_within = fg.col("a").exists_within(3, 3)

  assert exists_within(df).series_equal(
      pl.Series(
          "3_of_a_exists_within3",
          [False, False, True, True, True, False],
      ))

  abs_exists_within = fg.col("b").abs().exists_within(3, 3)
  assert abs_exists_within(df).series_equal(
      pl.Series(
          "3_of_(|b|)_exists_within3",
          [False, False, True, True, True, False],
      ))
