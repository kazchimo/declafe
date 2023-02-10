import polars as pl
import declafe.pl.feature_gen as fg


def test_divide_feature():
  df = pl.DataFrame({"a": [1, 2, 3, 4, 5, 6], "b": [1, 2, -3, 4, 5, 6]})

  div = fg.col("a") / fg.col("b")
  assert div(df).series_equal(
      pl.Series(
          "a_/_b",
          [1.0, 1.0, -1.0, 1.0, 1.0, 1.0],
      ))

  abs_div = fg.col("b").abs() / fg.col("a")
  assert abs_div(df).series_equal(
      pl.Series(
          "(|b|)_/_a",
          [1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
      ))

  div_const = fg.col("a") / 2
  assert div_const(df).series_equal(
      pl.Series(
          "a_/_2",
          [0.5, 1.0, 1.5, 2.0, 2.5, 3.0],
      ))

  div_lit = fg.col("a") / fg.lit(2)
  assert div_lit(df).series_equal(
      pl.Series(
          "a_/_2",
          [0.5, 1.0, 1.5, 2.0, 2.5, 3.0],
      ))


def test_rdivide_feature():
  df = pl.DataFrame({"a": [1, 2, 3, 4, 5, 6], "b": [1, 2, -3, 4, 5, 6]})

  rdiv = 2 / fg.col("a")
  assert rdiv(df).series_equal(
      pl.Series(
          "2_/_a",
          [2.0, 1.0, 0.6666666666666666, 0.5, 0.4, 0.3333333333333333],
      ))

  abs_rdiv = 2 / fg.col("b").abs()
  assert abs_rdiv(df).series_equal(
      pl.Series(
          "2_/_(|b|)",
          [2.0, 1.0, 0.6666666666666666, 0.5, 0.4, 0.3333333333333333],
      ))

  rdiv_const = fg.lit(2) / fg.col("a")
  assert rdiv_const(df).series_equal(
      pl.Series(
          "2_/_a",
          [2.0, 1.0, 0.6666666666666666, 0.5, 0.4, 0.3333333333333333],
      ))
