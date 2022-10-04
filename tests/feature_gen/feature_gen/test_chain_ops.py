import numpy as np
import pandas as pd
import talib

from declafe import col, c, FeatureGen, Features
from declafe.feature_gen.unary import LogFeature, SumFeature

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


class TestAccumulate:

  def test_accumulate(self):
    df = pd.DataFrame({"a": [1, 2, 3, 4, 5, 6]})
    f = a.accumulate("sum", lambda x, y: x + y)
    f2 = a.accumulate("find_latest_three", lambda x, y: x if x % 3 == 0 else y)

    f.generate(df).equals(pd.Series([1, 3, 6, 10, 15, 21]))
    f2.generate(df).equals(pd.Series([1, 2, 3, 3, 3, 6]))


class TestExistWithin:

  def test_exist_within(self):
    df = pd.DataFrame({"a": [1, 2, 3, 4, 5, 6]})
    f = a.exist_within(3, 3)

    assert f.generate(df).equals(
        pd.Series([False, False, True, True, True, False]))


class TestMinComp:

  def test_return_min_value(self):
    df = test_df.copy()
    result = a.min_comp(500).gen(df)
    pred = pd.Series(list(range(1, 501)) + [500] * 500)

    assert result.equals(pred)


class TestMaxComp:

  def test_return_max_value(self):
    df = test_df.copy()
    result = a.max_comp(500).gen(df)
    pred = pd.Series([500] * 500 + list(range(501, 1001)))

    assert result.equals(pred)


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
    assert _1.log().gen(test_df).equals(
        LogFeature("").gen_unary(pd.Series(1, index=test_df.index)))
    assert Double("a").log().gen(test_df).equals(
        LogFeature("").gen_unary(test_df["a"] * 2))


class TestMovingSums:

  def test_return_moving_sums(self):
    df1 = test_df.copy()
    df2 = test_df.copy()
    df1 = _1.set_feature(df1)
    df2 = _1.set_feature(df2)

    df1 = _1.moving_sums([3, 5]).set_features(df1)
    df2 = Features.many(SumFeature(3, _1.feature_name),
                        SumFeature(5, _1.feature_name)).set_features(df2)

    assert df1.equals(df2)


class TestAdd:

  def test_add(self):
    assert (a + 1).gen(test_df).equals(test_df["a"] + 1)


class TestApo:

  def test_calc_apo(self):
    assert a.apo(12, 26).gen(test_df).equals(talib.APO(test_df["a"], 12, 26))


class TestInvert:

  def test_invert(self):
    assert (~a).gen(pd.DataFrame({"a": [True, False]
                                 })).equals(pd.Series([False, True]))


class TestLag:

  def test_lag(self):
    assert a.lag(1).gen(test_df).equals(test_df["a"].shift(1))


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

    assert gen.gen(df).equals(pd.Series([0, 1, 2, 0, 1, 2, 3, 0, 1]))


class TestConsecutiveUpCount:

  def test_calc_consecutive_up_count(self):
    df = pd.DataFrame({"a": [1, 2, 3, 4, 5, 4, 3, 2, 1, 2]})
    gen = a.consecutive_up_count()

    assert gen.gen(df).equals(pd.Series([0, 1, 2, 3, 4, 0, 0, 0, 0, 1]))


class TestConsecutiveDownCount:

  def test_calc_consecutive_down_count(self):
    df = pd.DataFrame({"a": [1, 2, 3, 4, 5, 4, 3, 2, 1, 2]})
    gen = a.consecutive_down_count()

    assert gen.gen(df).equals(pd.Series([0, 0, 0, 0, 0, 1, 2, 3, 4, 0]))


class TestAbs:

  def test_abs(self):
    assert a.abs().gen(pd.DataFrame({"a": [-1, -2, -3, 4, 5, 6]
                                    })).equals(pd.Series([1, 2, 3, 4, 5, 6]))


class TestMACD:

  def test_calc_macd(self):
    assert a.macd(12, 26, 9)\
      .gen(test_df)\
      .equals(talib.MACD(test_df["a"], 12, 26, 9)[0])


class TestMACDSignal:

  def test_calc_macd_signal(self):
    assert a.macd_signal(12, 26, 9)\
      .gen(test_df)\
      .equals(talib.MACD(test_df["a"], 12, 26, 9)[1])


class TestMACDHist:

  def test_calc_macd_hist(self):
    assert a.macd_hist(12, 26, 9)\
      .gen(test_df)\
      .equals(talib.MACD(test_df["a"], 12, 26, 9)[2])


class TestMOM:

  def test_calc_mom(self):
    assert a.mom(10).gen(test_df).equals(talib.MOM(test_df["a"], 10))


class TestMOMS:

  def test_calc_moms(self):
    result = a.moms([10, 20]).set_features(test_df)

    assert result["MOM_10_of_a"].equals(talib.MOM(test_df["a"], 10))
    assert result["MOM_20_of_a"].equals(talib.MOM(test_df["a"], 20))


class TestRSI:

  def test_calc_rsi(self):
    assert a.rsi(10).gen(test_df).equals(talib.RSI(test_df["a"], 10))


class TestRSIs:

  def test_calc_rsis(self):
    result = a.rsis([10, 20]).set_features(test_df)

    assert result["RSI_10_of_a"].equals(talib.RSI(test_df["a"], 10))
    assert result["RSI_20_of_a"].equals(talib.RSI(test_df["a"], 20))


class TestPPO:

  def test_calc_ppo(self):
    assert a.ppo(26, 9).gen(test_df).equals(talib.PPO(test_df["a"], 26, 9))


class TestMaxWith:

  def test_max_with(self):
    df = pd.DataFrame({"c1": [1, 2, 3], "b": [0, 1, 4]})
    result = col("c1").max_with("b").gen(df)

    assert result.equals(pd.Series([1, 2, 4]))

  def test_accept_feature_gen(self):
    df = pd.DataFrame({"c1": [1, 2, 3], "b": [0, 1, 4]})
    result = col("c1").max_with(col("b")).gen(df)

    assert result.equals(pd.Series([1, 2, 4]))


class TestMinWith:

  def test_min_with(self):
    df = pd.DataFrame({"c1": [1, 2, 3], "b": [0, 1, 4]})
    result = col("c1").min_with("b").gen(df)

    assert result.equals(pd.Series([0, 1, 3]))

  def test_accept_feature_gen(self):
    df = pd.DataFrame({"c1": [1, 2, 3], "b": [0, 1, 4]})
    result = col("c1").min_with(col("b")).gen(df)

    assert result.equals(pd.Series([0, 1, 3]))


class TestSTOCHRSIFastk:

  def test_calc_stochrsi_fastk(self):
    assert a.stochrsi_fastk(10, 5, 3)\
      .gen(test_df)\
      .equals(talib.STOCHRSI(test_df["a"], 10, 5, 3)[0])


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
    assert a.trix(10).gen(test_df).equals(talib.TRIX(test_df["a"], 10))


class TestTRIXes:

  def test_calc_trixes(self):
    result = a.trixes([10, 20]).set_features(test_df)

    assert result["TRIX_10_of_a"].equals(talib.TRIX(test_df["a"], 10))
    assert result["TRIX_20_of_a"].equals(talib.TRIX(test_df["a"], 20))


class TestHT_DCPERIOD:

  def test_calc_ht_dcp(self):
    assert a.ht_dcperiod().gen(test_df).equals(talib.HT_DCPERIOD(test_df["a"]))


class TestHT_DCPHASE:

  def test_calc_ht_dcp(self):
    assert a.ht_dcphase().gen(test_df).equals(talib.HT_DCPHASE(test_df["a"]))


class TestHTPhasorInphase:

  def test_calc_ht_phasor_inphase(self):
    assert a.ht_phasor_inphase().gen(test_df).equals(
        talib.HT_PHASOR(test_df["a"])[0])


class TestHTPhasorQuadrature:

  def test_calc_ht_phasor_quadrature(self):
    assert a.ht_phasor_quadrature().gen(test_df).equals(
        talib.HT_PHASOR(test_df["a"])[1])


class TestHTSine:

  def test_calc_ht_sine(self):
    assert a.ht_sine().gen(test_df).equals(talib.HT_SINE(test_df["a"])[0])


class TestHTLeadSine:

  def test_calc_ht_sine(self):
    assert a.ht_leadsine().gen(test_df).equals(talib.HT_SINE(test_df["a"])[1])


class TestHTTrendmode:

  def test_calc_ht_trendmode(self):
    assert a.ht_trendmode().gen(test_df).equals(talib.HT_TRENDMODE(
        test_df["a"]))
