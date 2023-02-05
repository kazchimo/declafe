import polars as pl
import pl.feature_gen as fg


def test_then():
  df = pl.DataFrame({"a": [1, 2, 3, 4, 5, 6], "b": [1, 2, -3, 4, 5, 6]})

  mul_2 = fg.col("a").then(lambda s: s * 2, "mul_2")
  assert mul_2(df).series_equal(pl.Series(
      "mul_2(a)",
      [2, 4, 6, 8, 10, 12],
  ))

  abs_mul_2 = fg.col("b").abs().then(lambda s: s * 2, "mul_2")
  assert abs_mul_2(df).series_equal(
      pl.Series(
          "mul_2(|b|)",
          [2, 4, 6, 8, 10, 12],
      ))
