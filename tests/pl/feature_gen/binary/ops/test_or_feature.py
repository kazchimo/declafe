import polars as pl
import pl.feature_gen as fg


def test_or_feature():
  df = pl.DataFrame({
      "a": [True, False, True, False],
      "b": [True, True, False, False]
  })

  or_ = fg.col("a") | fg.col("b")
  assert or_(df).series_equal(pl.Series("a_|_b", [True, True, True, False]))

  or_const = fg.col("a") | True
  assert or_const(df).series_equal(
      pl.Series("a_|_True", [True, True, True, True]))

  or_lit = fg.col("a") | fg.lit(True)
  assert or_lit(df).series_equal(pl.Series("a_|_True",
                                           [True, True, True, True]))


def test_ror_feature():
  df = pl.DataFrame({
      "a": [True, False, True, False],
      "b": [True, True, False, False]
  })

  ror = True | fg.col("a")
  assert ror(df).series_equal(pl.Series("True_|_a", [True, True, True, True]))

  ror_const = fg.lit(True) | fg.col("a")
  assert ror_const(df).series_equal(
      pl.Series("True_|_a", [True, True, True, True]))
