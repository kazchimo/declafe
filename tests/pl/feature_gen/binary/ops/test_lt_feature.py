import polars as pl
import declafe.pl.feature_gen as fg


def test_lt_feature():
  df = pl.DataFrame({"a": [1, 2, 3, 4, 5, 6], "b": [1, 2, -3, 4, 5, 6]})

  lt = fg.col("a") < fg.col("b")
  assert lt(df).series_equal(
      pl.Series(
          "a_<_b",
          [False, False, False, False, False, False],
      ))

  lt_const = fg.col("a") < 2
  assert lt_const(df).series_equal(
      pl.Series(
          "a_<_2",
          [True, False, False, False, False, False],
      ))

  lt_lit = fg.col("a") < fg.lit(2)
  assert lt_lit(df).series_equal(
      pl.Series(
          "a_<_2",
          [True, False, False, False, False, False],
      ))
