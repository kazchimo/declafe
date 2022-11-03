import numpy as np
import pandas as pd
import talib

from declafe import col, c, FeatureGen, Features
from declafe.feature_gen.unary import LogFeature, SumFeature
from datetime import datetime

test_df = pd.DataFrame({
    "a": list(range(1, 1001)),
    "b": list(range(1001, 2001))
})

a = col("a")
b = col("b")
_1 = c(1)


class TestCond:

  def test_cond(self):
    df = pd.DataFrame({
        "cond": [True, False],
        "a": [1, 2],
        "b": [3, 4],
    })
    f = col("cond").of_cond(col("a"), col("b"))

    assert f.generate(df).equals(pd.Series([1, 4]))


class TestThen:

  def test_thena(self):
    df = pd.DataFrame({"a": [1, 2, 3, 4, 5]})
    f = Features.many(
        a.then(lambda s: s + 1, "plus_one"),
        a.then(lambda s: pd.Series(s).rolling(2).max(), "max_rolling"),
    )

    result = f.set_features(df)

    assert result["plus_one_of_a"].equals(pd.Series([2, 3, 4, 5, 6]))
    assert result["max_rolling_of_a"].equals(pd.Series([np.nan, 2, 3, 4, 5]))


class TestAccumulate:

  def test_accumulate(self):
    df = pd.DataFrame({"a": [1, 2, 3, 4, 5, 6]})
    f = a.accumulate("sum", lambda x, y: x + y)
    f2 = a.accumulate("find_latest_three", lambda x, y: y if y % 3 == 0 else x)

    print(f.generate(df))
    print(f2.generate(df))

    assert np.array_equal(f.generate(df), pd.Series([1, 3, 6, 10, 15, 21]))
    assert np.array_equal(f2.generate(df), pd.Series([1, 1, 3, 3, 3, 6]))


class TestExistWithin:

  def test_exist_within(self):
    df = pd.DataFrame({"a": [1, 2, 3, 4, 5, 6]})
    f = a.exist_within(3, 3)

    assert np.array_equal(
        f.generate(df),
        pd.Series([False, False, True, True, True, False]),
    )


class TestMinComp:

  def test_return_min_value(self):
    df = test_df.copy()
    result = a.min_comp(500).gen(df)
    pred = pd.Series(list(range(1, 501)) + [500] * 500)

    assert np.array_equal(result, pred)


class TestMaxComp:

  def test_return_max_value(self):
    df = test_df.copy()
    result = a.max_comp(500).gen(df)
    pred = pd.Series([500] * 500 + list(range(501, 1001)))

    assert np.array_equal(result, pred, True)


class Double(FeatureGen):

  def __init__(self, column: str):
    super().__init__()
    self.column = column

  def gen(self, df: pd.DataFrame) -> pd.Series:
    return df[self.column] * 2

  def _feature_name(self) -> str:
    return "double"


class TestLog:

  def test_return_log(self):
    assert np.array_equal(
        _1.log().gen(test_df),
        LogFeature("").gen_unary(pd.Series(1, index=test_df.index)))
    assert np.array_equal(
        Double("a").log().gen(test_df),
        LogFeature("").gen_unary(test_df["a"] * 2))


class TestMovingSums:

  def test_return_moving_sums(self):
    df = pd.DataFrame({"a": [1, 2, 3, 4, 5, 6]})
    df = a.moving_sums([2, 3]).set_features(df)

    assert df["sum_2_of_a"].equals(pd.Series([np.nan, 3, 5, 7, 9, 11]))
    assert df["sum_3_of_a"].equals(pd.Series([np.nan, np.nan, 6, 9, 12, 15]))


class TestMovingMax:

  def test_return_moving_max(self):
    f = a.moving_max(3)
    df = pd.DataFrame({"a": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]})

    assert np.array_equal(f.gen(df),
                          np.array([np.nan, np.nan, 3, 4, 5, 6, 7, 8, 9, 10]),
                          True)


class TestMovingMin:

  def test_return_moving_min(self):
    f = a.moving_min(3)
    df = pd.DataFrame({"a": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]})

    assert np.array_equal(f.gen(df),
                          np.array([np.nan, np.nan, 1, 2, 3, 4, 5, 6, 7, 8]),
                          True)


class TestAdd:

  def test_add(self):
    assert np.array_equal((a + 1).gen(test_df), test_df["a"] + 1)


class TestApo:

  def test_calc_apo(self):
    assert np.array_equal(
        a.apo(12, 26).gen(test_df), talib.APO(test_df["a"], 12, 26), True)


class TestInvert:

  def test_invert(self):
    assert np.array_equal((~a).gen(pd.DataFrame({"a": [True, False]})),
                          pd.Series([False, True]), True)


class TestLag:

  def test_lag(self):
    print(a.lag(1).generate(test_df))
    print(test_df["a"].shift(1).values)
    assert np.array_equal(a.lag(1).generate(test_df),
                          test_df["a"].shift(1).values,
                          equal_nan=True)


class TestReplace:

  def test_replace(self):
    gen = a.lag(1).replace(np.nan, 99999)
    assert list(gen.gen(test_df)) == [99999] + list(range(1, 1000))


class TestReplaceNa:

  def test_replace_na(self):
    gen = a.lag(1).replace_na(99999)
    assert list(gen.gen(test_df)) == [99999] + list(range(1, 1000))


class TestConsecutiveCountOf:

  def test_calc_consecutive_count(self):
    df = pd.DataFrame({"a": ["a", "b", "b", "c", "b", "b", "b", "a", "b"]})
    gen = a.consecutive_count_of("b")

    assert np.array_equal(gen.gen(df), pd.Series([0, 1, 2, 0, 1, 2, 3, 0, 1]),
                          True)


class TestConsecutiveUpCount:

  def test_calc_consecutive_up_count(self):
    df = pd.DataFrame({"a": [1, 2, 3, 4, 5, 4, 3, 2, 1, 2]})
    gen = a.consecutive_up_count()

    assert np.array_equal(gen.gen(df), pd.Series([0, 1, 2, 3, 4, 0, 0, 0, 0,
                                                  1]))


class TestConsecutiveDownCount:

  def test_calc_consecutive_down_count(self):
    df = pd.DataFrame({"a": [1, 2, 3, 4, 5, 4, 3, 2, 1, 2]})
    gen = a.consecutive_down_count()

    assert np.array_equal(gen.gen(df), pd.Series([0, 0, 0, 0, 0, 1, 2, 3, 4,
                                                  0]))


class TestAbs:

  def test_abs(self):
    assert np.array_equal(
        a.abs().gen(pd.DataFrame({"a": [-1, -2, -3, 4, 5, 6]})),
        pd.Series([1, 2, 3, 4, 5, 6]), True)


class TestMACD:

  def test_calc_macd(self):
    assert np.array_equal(
        a.macd(12, 26, 9).gen(test_df),
        talib.MACD(test_df["a"], 12, 26, 9)[0], True)


class TestMACDSignal:

  def test_calc_macd_signal(self):
    assert np.array_equal(
        a.macd_signal(12, 26, 9).gen(test_df),
        talib.MACD(test_df["a"], 12, 26, 9)[1], True)


class TestMACDHist:

  def test_calc_macd_hist(self):
    assert np.array_equal(
        a.macd_hist(12, 26, 9).gen(test_df),
        talib.MACD(test_df["a"], 12, 26, 9)[2], True)


class TestMOM:

  def test_calc_mom(self):
    assert np.array_equal(
        a.mom(10).gen(test_df), talib.MOM(test_df["a"], 10), True)


class TestMOMS:

  def test_calc_moms(self):
    result = a.moms([10, 20]).set_features(test_df)

    assert result["MOM_10_of_a"].equals(talib.MOM(test_df["a"], 10))
    assert result["MOM_20_of_a"].equals(talib.MOM(test_df["a"], 20))


class TestRSI:

  def test_calc_rsi(self):
    assert np.array_equal(
        a.rsi(10).gen(test_df), talib.RSI(test_df["a"], 10), True)


class TestRSIs:

  def test_calc_rsis(self):
    result = a.rsis([10, 20]).set_features(test_df)

    assert result["RSI_10_of_a"].equals(talib.RSI(test_df["a"], 10))
    assert result["RSI_20_of_a"].equals(talib.RSI(test_df["a"], 20))


class TestPPO:

  def test_calc_ppo(self):
    assert np.array_equal(
        a.ppo(26, 9).gen(test_df), talib.PPO(test_df["a"], 26, 9), True)


class TestMaxWith:

  def test_max_with(self):
    df = pd.DataFrame({"c1": [1, 2, 3], "b": [0, 1, 4]})
    result = col("c1").max_with("b").gen(df)

    assert np.array_equal(result, pd.Series([1, 2, 4]))

  def test_accept_feature_gen(self):
    df = pd.DataFrame({"c1": [1, 2, 3], "b": [0, 1, 4]})
    result = col("c1").max_with(col("b")).gen(df)

    assert np.array_equal(result, pd.Series([1, 2, 4]), True)


class TestMinWith:

  def test_min_with(self):
    df = pd.DataFrame({"c1": [1, 2, 3], "b": [0, 1, 4]})
    result = col("c1").min_with("b").gen(df)

    assert np.array_equal(result, pd.Series([0, 1, 3]))

  def test_accept_feature_gen(self):
    df = pd.DataFrame({"c1": [1, 2, 3], "b": [0, 1, 4]})
    result = col("c1").min_with(col("b")).gen(df)

    assert np.array_equal(result, pd.Series([0, 1, 3]), True)


class TestBbandsUpper:

  def test_calc_bbands_upper(self):
    assert np.array_equal(
        a.bbands_upper(5, 2).gen(test_df),
        (talib.BBANDS(test_df["a"], 5, 2)[0]), True)


class TestBbandsUppers:

  def test_calc_bbands_uppers(self):
    result = a.bbands_uppers([5, 10], 2).set_features(test_df)

    assert result["bbands_upper2_5_of_a"].equals(
        talib.BBANDS(test_df["a"], 5, 2)[0])
    assert result["bbands_upper2_10_of_a"].equals(
        talib.BBANDS(test_df["a"], 10, 2)[0])


class TestBBandsLower:

  def test_calc_bbands_lower(self):
    assert np.array_equal(
        a.bbands_lower(5, 2).gen(test_df),
        talib.BBANDS(test_df["a"], 5, 2)[2], True)


class TestBBandsLowers:

  def test_calc_bbands_lowers(self):
    result = a.bbands_lowers([5, 10], 2).set_features(test_df)

    assert result["bbands_lower2_5_of_a"].equals(
        talib.BBANDS(test_df["a"], 5, 2)[2])
    assert result["bbands_lower2_10_of_a"].equals(
        talib.BBANDS(test_df["a"], 10, 2)[2])


class TestSTOCHRSIFastk:

  def test_calc_stochrsi_fastk(self):
    assert np.array_equal(
        a.stochrsi_fastk(10, 5, 3).gen(test_df),
        (talib.STOCHRSI(test_df["a"], 10, 5, 3)[0]), True)


class TestSTOCHRSIFastks:

  def test_calc_stochrsi_fastks(self):
    result = a.stochrsi_fastks([10, 20], 5, 3).set_features(test_df)

    assert result["STOCHRSI_fastk_10_5_3_0_of_a"].equals(
        talib.STOCHRSI(test_df["a"], 10, 5, 3)[0])
    assert result["STOCHRSI_fastk_20_5_3_0_of_a"].equals(
        talib.STOCHRSI(test_df["a"], 20, 5, 3)[0])


class STOCHRSIFastd:

  def test_calc_stochrsi_fastd(self):
    assert a.stochrsi_fastd(10, 5, 3)\
      .gen(test_df)\
      .equals(talib.STOCHRSI(test_df["a"], 10, 5, 3)[1])


class STOCHRSIFastds:

  def test_calc_stochrsi_fastds(self):
    result = a.stochrsi_fastds([10, 20], 5, 3).set_features(test_df)

    assert result["STOCHRSI_fastd_10_5_3_0_of_a"].equals(
        talib.STOCHRSI(test_df["a"], 10, 5, 3)[1])
    assert result["STOCHRSI_fastd_20_5_3_0_of_a"].equals(
        talib.STOCHRSI(test_df["a"], 20, 5, 3)[1])


class TestTRIX:

  def test_calc_trix(self):
    assert np.array_equal(
        a.trix(10).gen(test_df), (talib.TRIX(test_df["a"], 10)), True)


class TestTRIXes:

  def test_calc_trixes(self):
    result = a.trixes([10, 20]).set_features(test_df)

    assert result["TRIX_10_of_a"].equals(talib.TRIX(test_df["a"], 10))
    assert result["TRIX_20_of_a"].equals(talib.TRIX(test_df["a"], 20))


class TestHT_DCPERIOD:

  def test_calc_ht_dcp(self):
    assert np.array_equal(a.ht_dcperiod().gen(test_df),
                          (talib.HT_DCPERIOD(test_df["a"])), True)


class TestHT_DCPHASE:

  def test_calc_ht_dcp(self):
    assert np.array_equal(a.ht_dcphase().gen(test_df),
                          (talib.HT_DCPHASE(test_df["a"])), True)


class TestHTPhasorInphase:

  def test_calc_ht_phasor_inphase(self):
    assert np.array_equal(a.ht_phasor_inphase().gen(test_df),
                          (talib.HT_PHASOR(test_df["a"])[0]), True)


class TestHTPhasorQuadrature:

  def test_calc_ht_phasor_quadrature(self):
    assert np.array_equal(a.ht_phasor_quadrature().gen(test_df),
                          (talib.HT_PHASOR(test_df["a"])[1]), True)


class TestHTSine:

  def test_calc_ht_sine(self):
    assert np.array_equal(a.ht_sine().gen(test_df),
                          (talib.HT_SINE(test_df["a"].values.astype(float))[0]),
                          True)


class TestHTLeadSine:

  def test_calc_ht_sine(self):
    assert np.array_equal(a.ht_leadsine().gen(test_df),
                          (talib.HT_SINE(test_df["a"])[1]), True)


class TestHTTrendmode:

  def test_calc_ht_trendmode(self):
    assert (a.ht_trendmode().gen(test_df) == (talib.HT_TRENDMODE(
        test_df["a"]))).all()


class TestSecond:

  def test_calc_second(self):
    df = pd.DataFrame(
        {"a": [
            datetime(2018, 1, 1, 0, 0, 0),
            datetime(2018, 1, 1, 0, 0, 1),
        ]})

    assert (a.second().gen(df) == pd.Series([0, 1])).all()


class TestMinute:

  def test_calc_minute(self):
    df = pd.DataFrame(
        {"a": [
            datetime(2018, 1, 1, 0, 0, 0),
            datetime(2018, 1, 1, 0, 1, 1),
        ]})

    assert (a.minute().gen(df) == (pd.Series([0, 1]))).all()


class TestMinuteN:

  def test_calc_minute_n(self):
    df = pd.DataFrame({
        "a": [
            datetime(2018, 1, 1, 0, 0, 0),
            datetime(2018, 1, 1, 0, 1, 1),
            datetime(2018, 1, 1, 0, 2, 2),
        ]
    })

    assert np.array_equal(a.minute_n(2).gen(df), pd.Series([True, False, True]))


class TestMinuteNs:

  def test_calc_minute_ns(self):
    df = pd.DataFrame({
        "a": [
            datetime(2018, 1, 1, 0, 0, 0),
            datetime(2018, 1, 1, 0, 1, 1),
            datetime(2018, 1, 1, 0, 2, 2),
            datetime(2018, 1, 1, 0, 3, 3),
        ]
    })

    result = a.minute_ns([2, 3]).set_features(df)

    assert result["minute_2_of_a"].equals(pd.Series([True, False, True, False]))
    assert result["minute_3_of_a"].equals(pd.Series([True, False, False, True]))


class TestHour:

  def test_calc_hour(self):
    df = pd.DataFrame(
        {"a": [
            datetime(2018, 1, 1, 0, 0, 0),
            datetime(2018, 1, 1, 1, 0, 1),
        ]})

    assert (a.hour().generate(df) == (np.array([0, 1]))).all()


class TestHourN:

  def test_calc_hour_n(self):
    df = pd.DataFrame({
        "a": [
            datetime(2018, 1, 1, 0, 0, 0),
            datetime(2018, 1, 1, 1, 1, 1),
            datetime(2018, 1, 1, 2, 2, 2),
        ]
    })

    assert np.array_equal(a.hour_n(2).gen(df), pd.Series([True, False, True]))


class TestHourNs:

  def test_calc_hour_ns(self):
    df = pd.DataFrame({
        "a": [
            datetime(2018, 1, 1, 0, 0, 0),
            datetime(2018, 1, 1, 1, 1, 1),
            datetime(2018, 1, 1, 2, 2, 2),
            datetime(2018, 1, 1, 3, 3, 3),
        ]
    })

    result = a.hour_ns([2, 3]).set_features(df, show_progress=True)

    assert result["hour_2_of_a"].equals(pd.Series([True, False, True, False]))
    assert result["hour_3_of_a"].equals(pd.Series([True, False, False, True]))


class TestDayOfWeek:

  def test_calc_day_of_week(self):
    df = pd.DataFrame(
        {"a": [
            datetime(2018, 1, 1, 0, 0, 0),
            datetime(2018, 1, 2, 0, 0, 1),
        ]})

    assert (a.day_of_week().gen(df) == (np.array([0, 1]))).all()


class TestDayOfMonth:

  def test_calc_day_of_month(self):
    df = pd.DataFrame({
        "a": [
            datetime(2018, 1, 1, 0, 0, 0),
            datetime(2018, 5, 2, 0, 0, 1),
            datetime(2018, 8, 3, 0, 0, 1),
        ]
    })

    assert (a.day_of_month().generate(df) == np.array([1, 2, 3])).all()


class TestMonth:

  def test_calc_month(self):
    df = pd.DataFrame({
        "a": [
            datetime(2018, 1, 1, 0, 0, 0),
            datetime(2018, 5, 2, 0, 0, 1),
            datetime(2018, 8, 3, 0, 0, 1),
        ]
    })

    assert (a.month().generate(df) == np.array([1, 5, 8])).all()


class ToDatetime:

  def test_to_datetime(self):
    df = pd.DataFrame({"a": [1665194183, 1665194184]})
    df2 = pd.DataFrame({"a": [1665194183000, 1665194184000]})

    assert a.to_datetime("s").gen(df).equals(
        pd.Series([
            datetime(2018, 1, 1, 0, 0, 0),
            datetime(2018, 1, 1, 1, 0, 0),
        ]))
    assert a.to_datetime("ms").gen(df2).equals(
        pd.Series([
            datetime(2018, 1, 1, 0, 0, 0),
            datetime(2018, 1, 1, 1, 0, 0),
        ]))
