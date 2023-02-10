import polars as pl
import pl.feature_gen as fg


def test_mod_feature():
  df = pl.DataFrame({"a": [1, 2, 3, 4, 5, 6], "b": [1, 2, -3, 4, 5, 6]})

  mod = fg.col("a") % fg.col("b")
  assert mod(df).series_equal(pl.Series(
      "a_%_b",
      [0, 0, 0, 0, 0, 0],
  ))

  mod_const = fg.col("a") % 2
  assert mod_const(df).series_equal(pl.Series(
      "a_%_2",
      [1, 0, 1, 0, 1, 0],
  ))

  mod_lit = fg.col("a") % fg.lit(2)
  assert mod_lit(df).series_equal(pl.Series(
      "a_%_2",
      [1, 0, 1, 0, 1, 0],
  ))


def test_rmod_feature():
  df = pl.DataFrame({"a": [1, 2, 3, 4, 5, 6], "b": [1, 2, -3, 4, 5, 6]})

  rmod = 2 % fg.col("a")
  assert rmod(df).series_equal(pl.Series(
      "2_%_a",
      [0, 0, 2, 2, 2, 2],
  ))

  rmod_const = fg.lit(2) % fg.col("a")
  assert rmod_const(df).series_equal(pl.Series(
      "2_%_a",
      [0, 0, 2, 2, 2, 2],
  ))
