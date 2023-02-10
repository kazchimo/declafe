import talib
import polars as pl
import pl.feature_gen as fg

df = pl.DataFrame({
    "close": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "open": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "high": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "low": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "volume": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
})


class TestPpo:

  def test_ppo(self):
    gen = fg.col("close").talib.ppo(fastperiod=3, slowperiod=3, matype=1)
    name = "PPO(3, 3, 1)(close)"
    assert gen(df).fill_nan(0).series_equal(
        talib.PPO(df["close"], fastperiod=3, slowperiod=3,
                  matype=1).alias(name).fill_nan(0))


class TestTrima:

  def test_trima(self):
    gen = fg.col("close").talib.trima(timeperiod=3)
    name = "TRIMA(3)(close)"
    assert gen(df).fill_nan(0).series_equal(
        talib.TRIMA(df["close"], timeperiod=3).alias(name).fill_nan(0))


class TestTema:

  def test_tema(self):
    gen = fg.col("close").talib.tema(timeperiod=3)
    name = "TEMA(3)(close)"
    assert gen(df).fill_nan(0).series_equal(
        talib.TEMA(df["close"], timeperiod=3).alias(name).fill_nan(0))


class TestHt_phasor_0:

  def test_ht_phasor_0(self):
    gen = fg.col("close").talib.ht_phasor_0()
    name = "HT_PHASOR_0()(close)"
    assert gen(df).fill_nan(0).series_equal(
        talib.HT_PHASOR(df["close"],)[0].alias(name).fill_nan(0))


class TestHt_phasor_1:

  def test_ht_phasor_1(self):
    gen = fg.col("close").talib.ht_phasor_1()
    name = "HT_PHASOR_1()(close)"
    assert gen(df).fill_nan(0).series_equal(
        talib.HT_PHASOR(df["close"],)[1].alias(name).fill_nan(0))


class TestHt_sine_0:

  def test_ht_sine_0(self):
    gen = fg.col("close").talib.ht_sine_0()
    name = "HT_SINE_0()(close)"
    assert gen(df).fill_nan(0).series_equal(
        talib.HT_SINE(df["close"],)[0].alias(name).fill_nan(0))


class TestHt_sine_1:

  def test_ht_sine_1(self):
    gen = fg.col("close").talib.ht_sine_1()
    name = "HT_SINE_1()(close)"
    assert gen(df).fill_nan(0).series_equal(
        talib.HT_SINE(df["close"],)[1].alias(name).fill_nan(0))


class TestWma:

  def test_wma(self):
    gen = fg.col("close").talib.wma(timeperiod=3)
    name = "WMA(3)(close)"
    assert gen(df).fill_nan(0).series_equal(
        talib.WMA(df["close"], timeperiod=3).alias(name).fill_nan(0))


class TestMacdext_0:

  def test_macdext_0(self):
    gen = fg.col("close").talib.macdext_0(fastperiod=3,
                                          fastmatype=1,
                                          slowperiod=3,
                                          slowmatype=1,
                                          signalperiod=3,
                                          signalmatype=1)
    name = "MACDEXT_0(3, 1, 3, 1, 3, 1)(close)"
    assert gen(df).fill_nan(0).series_equal(
        talib.MACDEXT(df["close"],
                      fastperiod=3,
                      fastmatype=1,
                      slowperiod=3,
                      slowmatype=1,
                      signalperiod=3,
                      signalmatype=1)[0].alias(name).fill_nan(0))


class TestMacdext_1:

  def test_macdext_1(self):
    gen = fg.col("close").talib.macdext_1(fastperiod=3,
                                          fastmatype=1,
                                          slowperiod=3,
                                          slowmatype=1,
                                          signalperiod=3,
                                          signalmatype=1)
    name = "MACDEXT_1(3, 1, 3, 1, 3, 1)(close)"
    assert gen(df).fill_nan(0).series_equal(
        talib.MACDEXT(df["close"],
                      fastperiod=3,
                      fastmatype=1,
                      slowperiod=3,
                      slowmatype=1,
                      signalperiod=3,
                      signalmatype=1)[1].alias(name).fill_nan(0))


class TestMacdext_2:

  def test_macdext_2(self):
    gen = fg.col("close").talib.macdext_2(fastperiod=3,
                                          fastmatype=1,
                                          slowperiod=3,
                                          slowmatype=1,
                                          signalperiod=3,
                                          signalmatype=1)
    name = "MACDEXT_2(3, 1, 3, 1, 3, 1)(close)"
    assert gen(df).fill_nan(0).series_equal(
        talib.MACDEXT(df["close"],
                      fastperiod=3,
                      fastmatype=1,
                      slowperiod=3,
                      slowmatype=1,
                      signalperiod=3,
                      signalmatype=1)[2].alias(name).fill_nan(0))


class TestBbands_0:

  def test_bbands_0(self):
    gen = fg.col("close").talib.bbands_0(timeperiod=3,
                                         nbdevup=1,
                                         nbdevdn=1,
                                         matype=1)
    name = "BBANDS_0(3, 1, 1, 1)(close)"
    assert gen(df).fill_nan(0).series_equal(
        talib.BBANDS(df["close"], timeperiod=3, nbdevup=1, nbdevdn=1,
                     matype=1)[0].alias(name).fill_nan(0))


class TestBbands_1:

  def test_bbands_1(self):
    gen = fg.col("close").talib.bbands_1(timeperiod=3,
                                         nbdevup=1,
                                         nbdevdn=1,
                                         matype=1)
    name = "BBANDS_1(3, 1, 1, 1)(close)"
    assert gen(df).fill_nan(0).series_equal(
        talib.BBANDS(df["close"], timeperiod=3, nbdevup=1, nbdevdn=1,
                     matype=1)[1].alias(name).fill_nan(0))


class TestBbands_2:

  def test_bbands_2(self):
    gen = fg.col("close").talib.bbands_2(timeperiod=3,
                                         nbdevup=1,
                                         nbdevdn=1,
                                         matype=1)
    name = "BBANDS_2(3, 1, 1, 1)(close)"
    assert gen(df).fill_nan(0).series_equal(
        talib.BBANDS(df["close"], timeperiod=3, nbdevup=1, nbdevdn=1,
                     matype=1)[2].alias(name).fill_nan(0))


class TestRsi:

  def test_rsi(self):
    gen = fg.col("close").talib.rsi(timeperiod=3)
    name = "RSI(3)(close)"
    assert gen(df).fill_nan(0).series_equal(
        talib.RSI(df["close"], timeperiod=3).alias(name).fill_nan(0))


class TestStddev:

  def test_stddev(self):
    gen = fg.col("close").talib.stddev(timeperiod=3, nbdev=1)
    name = "STDDEV(3, 1)(close)"
    assert gen(df).fill_nan(0).series_equal(
        talib.STDDEV(df["close"], timeperiod=3,
                     nbdev=1).alias(name).fill_nan(0))


class TestTrix:

  def test_trix(self):
    gen = fg.col("close").talib.trix(timeperiod=3)
    name = "TRIX(3)(close)"
    assert gen(df).fill_nan(0).series_equal(
        talib.TRIX(df["close"], timeperiod=3).alias(name).fill_nan(0))


class TestMama_0:

  def test_mama_0(self):
    gen = fg.col("close").talib.mama_0(fastlimit=0.5, slowlimit=0.05)
    name = "MAMA_0(0.5, 0.05)(close)"
    assert gen(df).fill_nan(0).series_equal(
        talib.MAMA(df["close"], fastlimit=0.5,
                   slowlimit=0.05)[0].alias(name).fill_nan(0))


class TestMama_1:

  def test_mama_1(self):
    gen = fg.col("close").talib.mama_1(fastlimit=0.5, slowlimit=0.05)
    name = "MAMA_1(0.5, 0.05)(close)"
    assert gen(df).fill_nan(0).series_equal(
        talib.MAMA(df["close"], fastlimit=0.5,
                   slowlimit=0.05)[1].alias(name).fill_nan(0))


class TestEma:

  def test_ema(self):
    gen = fg.col("close").talib.ema(timeperiod=3)
    name = "EMA(3)(close)"
    assert gen(df).fill_nan(0).series_equal(
        talib.EMA(df["close"], timeperiod=3).alias(name).fill_nan(0))


class TestHt_trendmode:

  def test_ht_trendmode(self):
    gen = fg.col("close").talib.ht_trendmode()
    name = "HT_TRENDMODE()(close)"
    assert gen(df).series_equal(talib.HT_TRENDMODE(df["close"],).alias(name))


class TestHt_dcphase:

  def test_ht_dcphase(self):
    gen = fg.col("close").talib.ht_dcphase()
    name = "HT_DCPHASE()(close)"
    assert gen(df).fill_nan(0).series_equal(
        talib.HT_DCPHASE(df["close"],).alias(name).fill_nan(0))


class TestMa:

  def test_ma(self):
    gen = fg.col("close").talib.ma(timeperiod=3, matype=1)
    name = "MA(3, 1)(close)"
    assert gen(df).fill_nan(0).series_equal(
        talib.MA(df["close"], timeperiod=3, matype=1).alias(name).fill_nan(0))


class TestHt_dcperiod:

  def test_ht_dcperiod(self):
    gen = fg.col("close").talib.ht_dcperiod()
    name = "HT_DCPERIOD()(close)"
    assert gen(df).fill_nan(0).series_equal(
        talib.HT_DCPERIOD(df["close"],).alias(name).fill_nan(0))


class TestMacd_0:

  def test_macd_0(self):
    gen = fg.col("close").talib.macd_0(fastperiod=3,
                                       slowperiod=3,
                                       signalperiod=3)
    name = "MACD_0(3, 3, 3)(close)"
    assert gen(df).fill_nan(0).series_equal(
        talib.MACD(df["close"], fastperiod=3, slowperiod=3,
                   signalperiod=3)[0].alias(name).fill_nan(0))


class TestMacd_1:

  def test_macd_1(self):
    gen = fg.col("close").talib.macd_1(fastperiod=3,
                                       slowperiod=3,
                                       signalperiod=3)
    name = "MACD_1(3, 3, 3)(close)"
    assert gen(df).fill_nan(0).series_equal(
        talib.MACD(df["close"], fastperiod=3, slowperiod=3,
                   signalperiod=3)[1].alias(name).fill_nan(0))


class TestMacd_2:

  def test_macd_2(self):
    gen = fg.col("close").talib.macd_2(fastperiod=3,
                                       slowperiod=3,
                                       signalperiod=3)
    name = "MACD_2(3, 3, 3)(close)"
    assert gen(df).fill_nan(0).series_equal(
        talib.MACD(df["close"], fastperiod=3, slowperiod=3,
                   signalperiod=3)[2].alias(name).fill_nan(0))


class TestKama:

  def test_kama(self):
    gen = fg.col("close").talib.kama(timeperiod=3)
    name = "KAMA(3)(close)"
    assert gen(df).fill_nan(0).series_equal(
        talib.KAMA(df["close"], timeperiod=3).alias(name).fill_nan(0))


class TestCmo:

  def test_cmo(self):
    gen = fg.col("close").talib.cmo(timeperiod=3)
    name = "CMO(3)(close)"
    assert gen(df).fill_nan(0).series_equal(
        talib.CMO(df["close"], timeperiod=3).alias(name).fill_nan(0))


class TestT3:

  def test_t3(self):
    gen = fg.col("close").talib.t3(timeperiod=3, vfactor=1)
    name = "T3(3, 1)(close)"
    assert gen(df).fill_nan(0).series_equal(
        talib.T3(df["close"], timeperiod=3, vfactor=1).alias(name).fill_nan(0))


class TestMacdfix_0:

  def test_macdfix_0(self):
    gen = fg.col("close").talib.macdfix_0(signalperiod=3)
    name = "MACDFIX_0(3)(close)"
    assert gen(df).fill_nan(0).series_equal(
        talib.MACDFIX(df["close"], signalperiod=3)[0].alias(name).fill_nan(0))


class TestMacdfix_1:

  def test_macdfix_1(self):
    gen = fg.col("close").talib.macdfix_1(signalperiod=3)
    name = "MACDFIX_1(3)(close)"
    assert gen(df).fill_nan(0).series_equal(
        talib.MACDFIX(df["close"], signalperiod=3)[1].alias(name).fill_nan(0))


class TestMacdfix_2:

  def test_macdfix_2(self):
    gen = fg.col("close").talib.macdfix_2(signalperiod=3)
    name = "MACDFIX_2(3)(close)"
    assert gen(df).fill_nan(0).series_equal(
        talib.MACDFIX(df["close"], signalperiod=3)[2].alias(name).fill_nan(0))


class TestApo:

  def test_apo(self):
    gen = fg.col("close").talib.apo(fastperiod=3, slowperiod=3, matype=1)
    name = "APO(3, 3, 1)(close)"
    assert gen(df).fill_nan(0).series_equal(
        talib.APO(df["close"], fastperiod=3, slowperiod=3,
                  matype=1).alias(name).fill_nan(0))


class TestMom:

  def test_mom(self):
    gen = fg.col("close").talib.mom(timeperiod=3)
    name = "MOM(3)(close)"
    assert gen(df).fill_nan(0).series_equal(
        talib.MOM(df["close"], timeperiod=3).alias(name).fill_nan(0))


class TestMidpoint:

  def test_midpoint(self):
    gen = fg.col("close").talib.midpoint(timeperiod=3)
    name = "MIDPOINT(3)(close)"
    assert gen(df).fill_nan(0).series_equal(
        talib.MIDPOINT(df["close"], timeperiod=3).alias(name).fill_nan(0))


class TestDema:

  def test_dema(self):
    gen = fg.col("close").talib.dema(timeperiod=3)
    name = "DEMA(3)(close)"
    assert gen(df).fill_nan(0).series_equal(
        talib.DEMA(df["close"], timeperiod=3).alias(name).fill_nan(0))


class TestStochrsi_0:

  def test_stochrsi_0(self):
    gen = fg.col("close").talib.stochrsi_0(timeperiod=3,
                                           fastk_period=3,
                                           fastd_period=3,
                                           fastd_matype=1)
    name = "STOCHRSI_0(3, 3, 3, 1)(close)"
    assert gen(df).fill_nan(0).series_equal(
        talib.STOCHRSI(df["close"],
                       timeperiod=3,
                       fastk_period=3,
                       fastd_period=3,
                       fastd_matype=1)[0].alias(name).fill_nan(0))


class TestStochrsi_1:

  def test_stochrsi_1(self):
    gen = fg.col("close").talib.stochrsi_1(timeperiod=3,
                                           fastk_period=3,
                                           fastd_period=3,
                                           fastd_matype=1)
    name = "STOCHRSI_1(3, 3, 3, 1)(close)"
    assert gen(df).fill_nan(0).series_equal(
        talib.STOCHRSI(df["close"],
                       timeperiod=3,
                       fastk_period=3,
                       fastd_period=3,
                       fastd_matype=1)[1].alias(name).fill_nan(0))


class TestHt_trendline:

  def test_ht_trendline(self):
    gen = fg.col("close").talib.ht_trendline()
    name = "HT_TRENDLINE()(close)"
    assert gen(df).fill_nan(0).series_equal(
        talib.HT_TRENDLINE(df["close"],).alias(name).fill_nan(0))


class TestSma:

  def test_sma(self):
    gen = fg.col("close").talib.sma(timeperiod=3)
    name = "SMA(3)(close)"
    assert gen(df).fill_nan(0).series_equal(
        talib.SMA(df["close"], timeperiod=3).alias(name).fill_nan(0))
