import polars as pl
import declafe.pl.feature_gen as fg


def test_ne_feature():
  df = pl.DataFrame({"a": [1, 2, 3, 4, 5, 6], "b": [1, 2, -3, 4, 5, 6]})

  ne = fg.col("a") != fg.col("b")
  assert ne(df).series_equal(
      pl.Series(
          "a_!=_b",
          [False, False, True, False, False, False],
      ))

  ne_const = fg.col("a") != 2
  assert ne_const(df).series_equal(
      pl.Series(
          "a_!=_2",
          [True, False, True, True, True, True],
      ))

  ne_lit = fg.col("a") != fg.lit(2)
  assert ne_lit(df).series_equal(
      pl.Series(
          "a_!=_2",
          [True, False, True, True, True, True],
      ))


def test_rne_feature():
  df = pl.DataFrame({"a": [1, 2, 3, 4, 5, 6], "b": [1, 2, -3, 4, 5, 6]})

  rne = 2 != fg.col("a")
  assert rne(df).series_equal(
      pl.Series(
          "a_!=_2",
          [True, False, True, True, True, True],
      ))

  rne_const = fg.lit(2) != fg.col("a")
  assert rne_const(df).series_equal(
      pl.Series(
          "2_!=_a",
          [True, False, True, True, True, True],
      ))
