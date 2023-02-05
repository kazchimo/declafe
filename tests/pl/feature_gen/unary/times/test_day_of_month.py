import polars as pl
import pl.feature_gen as fg


def test_day_of_month():
  df = pl.DataFrame({
      "a": [
          "2021-01-01",
          "2021-01-02",
          "2021-01-03",
          "2021-01-04",
      ]
  }).with_columns([
      pl.col("a").str.strptime(pl.Datetime, "%Y-%m-%d").suffix("_datetime"),
      pl.col("a").str.strptime(pl.Date, "%Y-%m-%d").suffix("_date"),
  ])

  day_of_month = fg.col("a_datetime").day_of_month()
  assert day_of_month(df).series_equal(
      pl.Series(
          "day_of_month(a_datetime)",
          [1, 2, 3, 4],
      ))

  day_of_month = fg.col("a_date").day_of_month()
  assert day_of_month(df).series_equal(
      pl.Series(
          "day_of_month(a_date)",
          [1, 2, 3, 4],
      ))
