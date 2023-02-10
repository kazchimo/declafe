import polars as pl
import pl.feature_gen as fg


def test_round_n_feature():
  df = pl.DataFrame({"a": [1.234, -2.345, 3.456, -4.567, 5.678]})
  round = fg.col("a").round_n(2)

  assert round(df).series_equal(
      pl.Series(
          "round2(a)",
          [1.23, -2.35, 3.46, -4.57, 5.68],
      ))

  abs_round2 = fg.col("a").abs().round_n(2)
  assert abs_round2(df).series_equal(
      pl.Series(
          "round2(|a|)",
          [1.23, 2.35, 3.46, 4.57, 5.68],
      ))
