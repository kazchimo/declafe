import polars as pl
import pl.feature_gen as fg


def test_le_feature():
  df = pl.DataFrame({"a": [1, 2, 3, 4, 5, 6], "b": [1, 2, -3, 4, 5, 6]})

  le = fg.col("a") <= fg.col("b")
  assert le(df).series_equal(
      pl.Series(
          "a_<=_b",
          [True, True, False, True, True, True],
      ))

  le_const = fg.col("a") <= 2
  assert le_const(df).series_equal(
      pl.Series(
          "a_<=_2",
          [True, True, False, False, False, False],
      ))

  le_lit = fg.col("a") <= fg.lit(2)
  assert le_lit(df).series_equal(
      pl.Series(
          "a_<=_2",
          [True, True, False, False, False, False],
      ))
