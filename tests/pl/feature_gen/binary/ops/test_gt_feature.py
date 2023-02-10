import polars as pl
import declafe.pl.feature_gen as fg


def test_gt_feature():
  df = pl.DataFrame({"a": [1, 2, 3, 4, 5, 6], "b": [1, 2, -3, 4, 5, 6]})

  gt = fg.col("a") > fg.col("b")
  assert gt(df).series_equal(
      pl.Series(
          "a_>_b",
          [False, False, True, False, False, False],
      ))

  gt_const = fg.col("a") > 2
  assert gt_const(df).series_equal(
      pl.Series(
          "a_>_2",
          [False, False, True, True, True, True],
      ))

  gt_lit = fg.col("a") > fg.lit(2)
  assert gt_lit(df).series_equal(
      pl.Series(
          "a_>_2",
          [False, False, True, True, True, True],
      ))
