import polars as pl
import declafe.pl.feature_gen as fg


def test_eq_feature():
  df = pl.DataFrame({"a": [1, 2, 3, 4, 5, 6], "b": [1, 2, -3, 4, 5, 6]})

  eq = fg.col("a") == fg.col("b")
  assert eq(df).series_equal(
      pl.Series(
          "a_==_b",
          [True, True, False, True, True, True],
      ))

  eq_const = fg.col("a") == 2
  assert eq_const(df).series_equal(
      pl.Series(
          "a_==_2",
          [False, True, False, False, False, False],
      ))

  eq_lit = fg.col("a") == fg.lit(2)
  assert eq_lit(df).series_equal(
      pl.Series(
          "a_==_2",
          [False, True, False, False, False, False],
      ))


def test_req_feature():
  df = pl.DataFrame({"a": [1, 2, 3, 4, 5, 6], "b": [1, 2, -3, 4, 5, 6]})

  req = 2 == fg.col("a")
  assert req(df).series_equal(
      pl.Series(
          "a_==_2",
          [False, True, False, False, False, False],
      ))

  req_const = fg.lit(2) == fg.col("a")
  assert req_const(df).series_equal(
      pl.Series(
          "2_==_a",
          [False, True, False, False, False, False],
      ))
