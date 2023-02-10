import polars as pl
import declafe.pl.feature_gen as fg


def test_week_of_year():
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

  week_of_year = fg.col("a_datetime").week_of_year()
  assert week_of_year(df).series_equal(
      pl.Series(
          "week_of_year(a_datetime)",
          [53, 53, 53, 1],
      ))

  week_of_year = fg.col("a_date").week_of_year()
  assert week_of_year(df).series_equal(
      pl.Series(
          "week_of_year(a_date)",
          [53, 53, 53, 1],
      ))

  df = pl.DataFrame({
      "a": [
          1612137600000000000,
          1612224000000000000,
          1612310400000000000,
          1612396800000000000,
      ]
  })
  week_of_year = fg.col("a").parse_unixtime("ns").week_of_year()
  assert week_of_year(df).series_equal(
      pl.Series(
          "week_of_year(parse_unixtime(a))",
          [5, 5, 5, 5],
      ))
