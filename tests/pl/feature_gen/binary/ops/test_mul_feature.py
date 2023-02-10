import polars as pl
import pl.feature_gen as fg


def test_mul():
  df = pl.DataFrame({"a": [1, 2, 3, 4, 5, 6], "b": [1, 2, -3, 4, 5, 6]})

  mul = fg.col("a") * fg.col("b")
  assert mul(df).series_equal(pl.Series(
      "a_*_b",
      [1, 4, -9, 16, 25, 36],
  ))

  abs_mul = fg.col("b").abs() * fg.col("a")
  assert abs_mul(df).series_equal(pl.Series(
      "(|b|)_*_a",
      [1, 4, 9, 16, 25, 36],
  ))

  mul_const = fg.col("a") * 2
  assert mul_const(df).series_equal(pl.Series(
      "a_*_2",
      [2, 4, 6, 8, 10, 12],
  ))

  mul_lit = fg.col("a") * fg.lit(2)
  assert mul_lit(df).series_equal(pl.Series(
      "a_*_2",
      [2, 4, 6, 8, 10, 12],
  ))


def test_rmul():
  df = pl.DataFrame({"a": [1, 2, 3, 4, 5, 6], "b": [1, 2, -3, 4, 5, 6]})

  rmul = 2 * fg.col("a")
  assert rmul(df).series_equal(pl.Series(
      "2_*_a",
      [2, 4, 6, 8, 10, 12],
  ))

  abs_rmul = 2 * fg.col("b").abs()
  assert abs_rmul(df).series_equal(pl.Series(
      "2_*_(|b|)",
      [2, 4, 6, 8, 10, 12],
  ))

  rmul_const = fg.lit(2) * fg.col("a")
  assert rmul_const(df).series_equal(pl.Series(
      "2_*_a",
      [2, 4, 6, 8, 10, 12],
  ))
