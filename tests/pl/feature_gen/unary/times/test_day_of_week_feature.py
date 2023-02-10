import polars as pl
import pl.feature_gen as fg


def test_day_of_week():
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

  day_of_week = fg.col("a_datetime").day_of_week()
  assert day_of_week(df).series_equal(
      pl.Series(
          "day_of_week(a_datetime)",
          [5, 6, 7, 1],
      ))

  day_of_week = fg.col("a_date").day_of_week()
  assert day_of_week(df).series_equal(
      pl.Series(
          "day_of_week(a_date)",
          [5, 6, 7, 1],
      ))

  df = pl.DataFrame({
      "a": [
          1612137600000000000,
          1612224000000000000,
          1612310400000000000,
          1612396800000000000,
      ]
  })
  day_of_week = fg.col("a").parse_unixtime("ns").day_of_week()
  assert day_of_week(df).series_equal(
      pl.Series(
          "day_of_week(parse_unixtime(a))",
          [1, 2, 3, 4],
      ))
