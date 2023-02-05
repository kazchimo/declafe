import polars as pl
import pl.feature_gen as fg


def test_and_feature():
  df = pl.DataFrame({
      "a": [True, False, True, False],
      "b": [True, True, False, False]
  })
  and_ = fg.col("a") & fg.col("b")
  assert and_(df).series_equal(pl.Series(
      "a_&_b",
      [True, False, False, False],
  ))

  and_const = fg.col("a") & True
  assert and_const(df).series_equal(
      pl.Series(
          "a_&_True",
          [True, False, True, False],
      ))

  and_lit = fg.col("a") & fg.lit(True)
  assert and_lit(df).series_equal(
      pl.Series(
          "a_&_True",
          [True, False, True, False],
      ))


def test_rand_feature():
  df = pl.DataFrame({
      "a": [True, False, True, False],
      "b": [True, True, False, False]
  })

  rand = True & fg.col("a")
  assert rand(df).series_equal(
      pl.Series(
          "True_&_a",
          [True, False, True, False],
      ))

  rand_const = fg.lit(True) & fg.col("a")
  assert rand_const(df).series_equal(
      pl.Series(
          "True_&_a",
          [True, False, True, False],
      ))
