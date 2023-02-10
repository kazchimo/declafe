import polars as pl
import declafe.pl.feature_gen as fg


def test_hour_feature():
  df = pl.DataFrame({
      "a": [
          "2021-01-01 01:11:11",
          "2021-01-02 02:22:22",
          "2021-01-03 03:33:33",
          "2021-01-04 04:44:44",
      ]
  }).with_columns([
      pl.col("a").str.strptime(pl.Datetime,
                               "%Y-%m-%d %H:%M:%S").suffix("_datetime"),
      pl.col("a").str.strptime(pl.Date, "%Y-%m-%d %H:%M:%S").suffix("_date"),
  ])

  hour = fg.col("a_datetime").hour()
  assert hour(df).series_equal(pl.Series(
      "hour(a_datetime)",
      [1, 2, 3, 4],
  ))

  df = pl.DataFrame({
      "a": [
          1612141871000000000,
          1612232542000000000,
          1612323213000000000,
          1612413884000000000,
      ]
  })
  hour = fg.col("a").parse_unixtime("ns").hour()
  assert hour(df).series_equal(
      pl.Series(
          "hour(parse_unixtime(a))",
          [1, 2, 3, 4],
      ))
