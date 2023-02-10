import polars as pl
import pl.feature_gen as fg


def test_ge_feature():
  df = pl.DataFrame({"a": [1, 2, 3, 4, 5, 6], "b": [1, 2, -3, 4, 5, 6]})

  ge = fg.col("a") >= fg.col("b")
  assert ge(df).series_equal(
      pl.Series(
          "a_>=_b",
          [True, True, True, True, True, True],
      ))

  ge_const = fg.col("a") >= 2
  assert ge_const(df).series_equal(
      pl.Series(
          "a_>=_2",
          [False, True, True, True, True, True],
      ))

  ge_lit = fg.col("a") >= fg.lit(2)
  assert ge_lit(df).series_equal(
      pl.Series(
          "a_>=_2",
          [False, True, True, True, True, True],
      ))
