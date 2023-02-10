import polars as pl
import declafe.pl.feature_gen as fg


def test_month():
  df = pl.DataFrame({
      "a": [
          "2021-01-01",
          "2021-02-02",
          "2021-03-03",
          "2021-04-04",
      ]
  }).with_columns([
      pl.col("a").str.strptime(pl.Datetime, "%Y-%m-%d").suffix("_datetime"),
      pl.col("a").str.strptime(pl.Date, "%Y-%m-%d").suffix("_date"),
  ])

  month = fg.col("a_datetime").month()
  assert month(df).series_equal(pl.Series(
      "month(a_datetime)",
      [1, 2, 3, 4],
  ))

  month = fg.col("a_date").month()
  assert month(df).series_equal(pl.Series(
      "month(a_date)",
      [1, 2, 3, 4],
  ))

  df = pl.DataFrame({
      "a": [
          1612137600000000000,
          1612224000000000000,
          1612310400000000000,
          1612396800000000000,
      ]
  })
  month = fg.col("a").parse_unixtime("ns").month()
  assert month(df).series_equal(
      pl.Series(
          "month(parse_unixtime(a))",
          [2, 2, 2, 2],
      ))
