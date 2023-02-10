import talib
import polars as pl
import declafe.pl.feature_gen as fg
import numpy as np

df = pl.DataFrame({
    "close": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "open": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "high": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "low": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "volume": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
})


class TestDx:

  def test_dx(self):
    gen = fg.talib.dx(fg.col("high"),
                      fg.col("low"),
                      fg.col("close"),
                      timeperiod=3)
    name = "DX(3)(high, low, close)"
    assert np.array_equal(gen(df).to_numpy(),
                          talib.DX(df["high"],
                                   df["low"],
                                   df["close"],
                                   timeperiod=3).alias(name),
                          equal_nan=True)


class TestTrange:

  def test_trange(self):
    gen = fg.talib.trange(fg.col("high"), fg.col("low"), fg.col("close"))
    name = "TRANGE()(high, low, close)"
    assert np.array_equal(gen(df).to_numpy(),
                          talib.TRANGE(df["high"], df["low"],
                                       df["close"]).alias(name),
                          equal_nan=True)


class TestNatr:

  def test_natr(self):
    gen = fg.talib.natr(fg.col("high"),
                        fg.col("low"),
                        fg.col("close"),
                        timeperiod=3)
    name = "NATR(3)(high, low, close)"
    assert np.array_equal(gen(df).to_numpy(),
                          talib.NATR(df["high"],
                                     df["low"],
                                     df["close"],
                                     timeperiod=3).alias(name),
                          equal_nan=True)


class TestWillr:

  def test_willr(self):
    gen = fg.talib.willr(fg.col("high"),
                         fg.col("low"),
                         fg.col("close"),
                         timeperiod=3)
    name = "WILLR(3)(high, low, close)"
    assert np.array_equal(gen(df).to_numpy(),
                          talib.WILLR(df["high"],
                                      df["low"],
                                      df["close"],
                                      timeperiod=3).alias(name),
                          equal_nan=True)


class TestAdxr:

  def test_adxr(self):
    gen = fg.talib.adxr(fg.col("high"),
                        fg.col("low"),
                        fg.col("close"),
                        timeperiod=3)
    name = "ADXR(3)(high, low, close)"
    assert np.array_equal(gen(df).to_numpy(),
                          talib.ADXR(df["high"],
                                     df["low"],
                                     df["close"],
                                     timeperiod=3).alias(name),
                          equal_nan=True)


class TestStoch_0:

  def test_stoch_0(self):
    gen = fg.talib.stoch_0(fg.col("high"),
                           fg.col("low"),
                           fg.col("close"),
                           fastk_period=3,
                           slowk_period=3,
                           slowk_matype=1,
                           slowd_period=3,
                           slowd_matype=1)
    name = "STOCH_0(3, 3, 1, 3, 1)(high, low, close)"
    assert np.array_equal(gen(df).to_numpy(),
                          talib.STOCH(df["high"],
                                      df["low"],
                                      df["close"],
                                      fastk_period=3,
                                      slowk_period=3,
                                      slowk_matype=1,
                                      slowd_period=3,
                                      slowd_matype=1)[0].alias(name),
                          equal_nan=True)


class TestStoch_1:

  def test_stoch_1(self):
    gen = fg.talib.stoch_1(fg.col("high"),
                           fg.col("low"),
                           fg.col("close"),
                           fastk_period=3,
                           slowk_period=3,
                           slowk_matype=1,
                           slowd_period=3,
                           slowd_matype=1)
    name = "STOCH_1(3, 3, 1, 3, 1)(high, low, close)"
    assert np.array_equal(gen(df).to_numpy(),
                          talib.STOCH(df["high"],
                                      df["low"],
                                      df["close"],
                                      fastk_period=3,
                                      slowk_period=3,
                                      slowk_matype=1,
                                      slowd_period=3,
                                      slowd_matype=1)[1].alias(name),
                          equal_nan=True)


class TestMinus_di:

  def test_minus_di(self):
    gen = fg.talib.minus_di(fg.col("high"),
                            fg.col("low"),
                            fg.col("close"),
                            timeperiod=3)
    name = "MINUS_DI(3)(high, low, close)"
    assert np.array_equal(gen(df).to_numpy(),
                          talib.MINUS_DI(df["high"],
                                         df["low"],
                                         df["close"],
                                         timeperiod=3).alias(name),
                          equal_nan=True)


class TestStochf_0:

  def test_stochf_0(self):
    gen = fg.talib.stochf_0(fg.col("high"),
                            fg.col("low"),
                            fg.col("close"),
                            fastk_period=3,
                            fastd_period=3,
                            fastd_matype=1)
    name = "STOCHF_0(3, 3, 1)(high, low, close)"
    assert np.array_equal(gen(df).to_numpy(),
                          talib.STOCHF(df["high"],
                                       df["low"],
                                       df["close"],
                                       fastk_period=3,
                                       fastd_period=3,
                                       fastd_matype=1)[0].alias(name),
                          equal_nan=True)


class TestStochf_1:

  def test_stochf_1(self):
    gen = fg.talib.stochf_1(fg.col("high"),
                            fg.col("low"),
                            fg.col("close"),
                            fastk_period=3,
                            fastd_period=3,
                            fastd_matype=1)
    name = "STOCHF_1(3, 3, 1)(high, low, close)"
    assert np.array_equal(gen(df).to_numpy(),
                          talib.STOCHF(df["high"],
                                       df["low"],
                                       df["close"],
                                       fastk_period=3,
                                       fastd_period=3,
                                       fastd_matype=1)[1].alias(name),
                          equal_nan=True)


class TestCci:

  def test_cci(self):
    gen = fg.talib.cci(fg.col("high"),
                       fg.col("low"),
                       fg.col("close"),
                       timeperiod=3)
    name = "CCI(3)(high, low, close)"
    assert np.array_equal(gen(df).to_numpy(),
                          talib.CCI(df["high"],
                                    df["low"],
                                    df["close"],
                                    timeperiod=3).alias(name),
                          equal_nan=True)


class TestUltosc:

  def test_ultosc(self):
    gen = fg.talib.ultosc(fg.col("high"),
                          fg.col("low"),
                          fg.col("close"),
                          timeperiod1=3,
                          timeperiod2=3,
                          timeperiod3=3)
    name = "ULTOSC(3, 3, 3)(high, low, close)"
    assert np.array_equal(gen(df).to_numpy(),
                          talib.ULTOSC(df["high"],
                                       df["low"],
                                       df["close"],
                                       timeperiod1=3,
                                       timeperiod2=3,
                                       timeperiod3=3).alias(name),
                          equal_nan=True)


class TestAtr:

  def test_atr(self):
    gen = fg.talib.atr(fg.col("high"),
                       fg.col("low"),
                       fg.col("close"),
                       timeperiod=3)
    name = "ATR(3)(high, low, close)"
    assert np.array_equal(gen(df).to_numpy(),
                          talib.ATR(df["high"],
                                    df["low"],
                                    df["close"],
                                    timeperiod=3).alias(name),
                          equal_nan=True)


class TestPlus_di:

  def test_plus_di(self):
    gen = fg.talib.plus_di(fg.col("high"),
                           fg.col("low"),
                           fg.col("close"),
                           timeperiod=3)
    name = "PLUS_DI(3)(high, low, close)"
    assert np.array_equal(gen(df).to_numpy(),
                          talib.PLUS_DI(df["high"],
                                        df["low"],
                                        df["close"],
                                        timeperiod=3).alias(name),
                          equal_nan=True)


class TestAdx:

  def test_adx(self):
    gen = fg.talib.adx(fg.col("high"),
                       fg.col("low"),
                       fg.col("close"),
                       timeperiod=3)
    name = "ADX(3)(high, low, close)"
    assert np.array_equal(gen(df).to_numpy(),
                          talib.ADX(df["high"],
                                    df["low"],
                                    df["close"],
                                    timeperiod=3).alias(name),
                          equal_nan=True)


class TestCdlbreakaway:

  def test_cdlbreakaway(self):
    gen = fg.talib.cdlbreakaway(fg.col("open"), fg.col("high"), fg.col("low"),
                                fg.col("close"))
    name = "CDLBREAKAWAY()(open, high, low, close)"
    assert np.array_equal(gen(df).to_numpy(),
                          talib.CDLBREAKAWAY(df["open"], df["high"], df["low"],
                                             df["close"]).alias(name),
                          equal_nan=True)


class TestCdlrickshawman:

  def test_cdlrickshawman(self):
    gen = fg.talib.cdlrickshawman(fg.col("open"), fg.col("high"), fg.col("low"),
                                  fg.col("close"))
    name = "CDLRICKSHAWMAN()(open, high, low, close)"
    assert np.array_equal(gen(df).to_numpy(),
                          talib.CDLRICKSHAWMAN(df["open"], df["high"],
                                               df["low"],
                                               df["close"]).alias(name),
                          equal_nan=True)


class TestCdlmorningdojistar:

  def test_cdlmorningdojistar(self):
    gen = fg.talib.cdlmorningdojistar(fg.col("open"),
                                      fg.col("high"),
                                      fg.col("low"),
                                      fg.col("close"),
                                      penetration=1)
    name = "CDLMORNINGDOJISTAR(1)(open, high, low, close)"
    assert np.array_equal(gen(df).to_numpy(),
                          talib.CDLMORNINGDOJISTAR(df["open"],
                                                   df["high"],
                                                   df["low"],
                                                   df["close"],
                                                   penetration=1).alias(name),
                          equal_nan=True)


class TestCdl3starsinsouth:

  def test_cdl3starsinsouth(self):
    gen = fg.talib.cdl3starsinsouth(fg.col("open"), fg.col("high"),
                                    fg.col("low"), fg.col("close"))
    name = "CDL3STARSINSOUTH()(open, high, low, close)"
    assert np.array_equal(gen(df).to_numpy(),
                          talib.CDL3STARSINSOUTH(df["open"], df["high"],
                                                 df["low"],
                                                 df["close"]).alias(name),
                          equal_nan=True)


class TestCdlladderbottom:

  def test_cdlladderbottom(self):
    gen = fg.talib.cdlladderbottom(fg.col("open"), fg.col("high"),
                                   fg.col("low"), fg.col("close"))
    name = "CDLLADDERBOTTOM()(open, high, low, close)"
    assert np.array_equal(gen(df).to_numpy(),
                          talib.CDLLADDERBOTTOM(df["open"], df["high"],
                                                df["low"],
                                                df["close"]).alias(name),
                          equal_nan=True)


class TestCdldarkcloudcover:

  def test_cdldarkcloudcover(self):
    gen = fg.talib.cdldarkcloudcover(fg.col("open"),
                                     fg.col("high"),
                                     fg.col("low"),
                                     fg.col("close"),
                                     penetration=1)
    name = "CDLDARKCLOUDCOVER(1)(open, high, low, close)"
    assert np.array_equal(gen(df).to_numpy(),
                          talib.CDLDARKCLOUDCOVER(df["open"],
                                                  df["high"],
                                                  df["low"],
                                                  df["close"],
                                                  penetration=1).alias(name),
                          equal_nan=True)


class TestCdlpiercing:

  def test_cdlpiercing(self):
    gen = fg.talib.cdlpiercing(fg.col("open"), fg.col("high"), fg.col("low"),
                               fg.col("close"))
    name = "CDLPIERCING()(open, high, low, close)"
    assert np.array_equal(gen(df).to_numpy(),
                          talib.CDLPIERCING(df["open"], df["high"], df["low"],
                                            df["close"]).alias(name),
                          equal_nan=True)


class TestCdlstalledpattern:

  def test_cdlstalledpattern(self):
    gen = fg.talib.cdlstalledpattern(fg.col("open"), fg.col("high"),
                                     fg.col("low"), fg.col("close"))
    name = "CDLSTALLEDPATTERN()(open, high, low, close)"
    assert np.array_equal(gen(df).to_numpy(),
                          talib.CDLSTALLEDPATTERN(df["open"], df["high"],
                                                  df["low"],
                                                  df["close"]).alias(name),
                          equal_nan=True)


class TestCdlinneck:

  def test_cdlinneck(self):
    gen = fg.talib.cdlinneck(fg.col("open"), fg.col("high"), fg.col("low"),
                             fg.col("close"))
    name = "CDLINNECK()(open, high, low, close)"
    assert np.array_equal(gen(df).to_numpy(),
                          talib.CDLINNECK(df["open"], df["high"], df["low"],
                                          df["close"]).alias(name),
                          equal_nan=True)


class TestCdlgravestonedoji:

  def test_cdlgravestonedoji(self):
    gen = fg.talib.cdlgravestonedoji(fg.col("open"), fg.col("high"),
                                     fg.col("low"), fg.col("close"))
    name = "CDLGRAVESTONEDOJI()(open, high, low, close)"
    assert np.array_equal(gen(df).to_numpy(),
                          talib.CDLGRAVESTONEDOJI(df["open"], df["high"],
                                                  df["low"],
                                                  df["close"]).alias(name),
                          equal_nan=True)


class TestCdl3linestrike:

  def test_cdl3linestrike(self):
    gen = fg.talib.cdl3linestrike(fg.col("open"), fg.col("high"), fg.col("low"),
                                  fg.col("close"))
    name = "CDL3LINESTRIKE()(open, high, low, close)"
    assert np.array_equal(gen(df).to_numpy(),
                          talib.CDL3LINESTRIKE(df["open"], df["high"],
                                               df["low"],
                                               df["close"]).alias(name),
                          equal_nan=True)


class TestCdlabandonedbaby:

  def test_cdlabandonedbaby(self):
    gen = fg.talib.cdlabandonedbaby(fg.col("open"),
                                    fg.col("high"),
                                    fg.col("low"),
                                    fg.col("close"),
                                    penetration=1)
    name = "CDLABANDONEDBABY(1)(open, high, low, close)"
    assert np.array_equal(gen(df).to_numpy(),
                          talib.CDLABANDONEDBABY(df["open"],
                                                 df["high"],
                                                 df["low"],
                                                 df["close"],
                                                 penetration=1).alias(name),
                          equal_nan=True)


class TestCdl2crows:

  def test_cdl2crows(self):
    gen = fg.talib.cdl2crows(fg.col("open"), fg.col("high"), fg.col("low"),
                             fg.col("close"))
    name = "CDL2CROWS()(open, high, low, close)"
    assert np.array_equal(gen(df).to_numpy(),
                          talib.CDL2CROWS(df["open"], df["high"], df["low"],
                                          df["close"]).alias(name),
                          equal_nan=True)


class TestCdlunique3river:

  def test_cdlunique3river(self):
    gen = fg.talib.cdlunique3river(fg.col("open"), fg.col("high"),
                                   fg.col("low"), fg.col("close"))
    name = "CDLUNIQUE3RIVER()(open, high, low, close)"
    assert np.array_equal(gen(df).to_numpy(),
                          talib.CDLUNIQUE3RIVER(df["open"], df["high"],
                                                df["low"],
                                                df["close"]).alias(name),
                          equal_nan=True)


class TestCdl3blackcrows:

  def test_cdl3blackcrows(self):
    gen = fg.talib.cdl3blackcrows(fg.col("open"), fg.col("high"), fg.col("low"),
                                  fg.col("close"))
    name = "CDL3BLACKCROWS()(open, high, low, close)"
    assert np.array_equal(gen(df).to_numpy(),
                          talib.CDL3BLACKCROWS(df["open"], df["high"],
                                               df["low"],
                                               df["close"]).alias(name),
                          equal_nan=True)


class TestMfi:

  def test_mfi(self):
    gen = fg.talib.mfi(fg.col("high"),
                       fg.col("low"),
                       fg.col("close"),
                       fg.col("volume"),
                       timeperiod=3)
    name = "MFI(3)(high, low, close, volume)"
    assert np.array_equal(gen(df).to_numpy(),
                          talib.MFI(df["high"],
                                    df["low"],
                                    df["close"],
                                    df["volume"],
                                    timeperiod=3).alias(name),
                          equal_nan=True)


class TestCdlhomingpigeon:

  def test_cdlhomingpigeon(self):
    gen = fg.talib.cdlhomingpigeon(fg.col("open"), fg.col("high"),
                                   fg.col("low"), fg.col("close"))
    name = "CDLHOMINGPIGEON()(open, high, low, close)"
    assert np.array_equal(gen(df).to_numpy(),
                          talib.CDLHOMINGPIGEON(df["open"], df["high"],
                                                df["low"],
                                                df["close"]).alias(name),
                          equal_nan=True)


class TestAdosc:

  def test_adosc(self):
    gen = fg.talib.adosc(fg.col("high"),
                         fg.col("low"),
                         fg.col("close"),
                         fg.col("volume"),
                         fastperiod=3,
                         slowperiod=3)
    name = "ADOSC(3, 3)(high, low, close, volume)"
    assert np.array_equal(gen(df).to_numpy(),
                          talib.ADOSC(df["high"],
                                      df["low"],
                                      df["close"],
                                      df["volume"],
                                      fastperiod=3,
                                      slowperiod=3).alias(name),
                          equal_nan=True)


class TestCdlcounterattack:

  def test_cdlcounterattack(self):
    gen = fg.talib.cdlcounterattack(fg.col("open"), fg.col("high"),
                                    fg.col("low"), fg.col("close"))
    name = "CDLCOUNTERATTACK()(open, high, low, close)"
    assert np.array_equal(gen(df).to_numpy(),
                          talib.CDLCOUNTERATTACK(df["open"], df["high"],
                                                 df["low"],
                                                 df["close"]).alias(name),
                          equal_nan=True)


class TestCdlidentical3crows:

  def test_cdlidentical3crows(self):
    gen = fg.talib.cdlidentical3crows(fg.col("open"), fg.col("high"),
                                      fg.col("low"), fg.col("close"))
    name = "CDLIDENTICAL3CROWS()(open, high, low, close)"
    assert np.array_equal(gen(df).to_numpy(),
                          talib.CDLIDENTICAL3CROWS(df["open"], df["high"],
                                                   df["low"],
                                                   df["close"]).alias(name),
                          equal_nan=True)


class TestCdlmorningstar:

  def test_cdlmorningstar(self):
    gen = fg.talib.cdlmorningstar(fg.col("open"),
                                  fg.col("high"),
                                  fg.col("low"),
                                  fg.col("close"),
                                  penetration=1)
    name = "CDLMORNINGSTAR(1)(open, high, low, close)"
    assert np.array_equal(gen(df).to_numpy(),
                          talib.CDLMORNINGSTAR(df["open"],
                                               df["high"],
                                               df["low"],
                                               df["close"],
                                               penetration=1).alias(name),
                          equal_nan=True)


class TestCdllongleggeddoji:

  def test_cdllongleggeddoji(self):
    gen = fg.talib.cdllongleggeddoji(fg.col("open"), fg.col("high"),
                                     fg.col("low"), fg.col("close"))
    name = "CDLLONGLEGGEDDOJI()(open, high, low, close)"
    assert np.array_equal(gen(df).to_numpy(),
                          talib.CDLLONGLEGGEDDOJI(df["open"], df["high"],
                                                  df["low"],
                                                  df["close"]).alias(name),
                          equal_nan=True)


class TestCdlseparatinglines:

  def test_cdlseparatinglines(self):
    gen = fg.talib.cdlseparatinglines(fg.col("open"), fg.col("high"),
                                      fg.col("low"), fg.col("close"))
    name = "CDLSEPARATINGLINES()(open, high, low, close)"
    assert np.array_equal(gen(df).to_numpy(),
                          talib.CDLSEPARATINGLINES(df["open"], df["high"],
                                                   df["low"],
                                                   df["close"]).alias(name),
                          equal_nan=True)


class TestCdlspinningtop:

  def test_cdlspinningtop(self):
    gen = fg.talib.cdlspinningtop(fg.col("open"), fg.col("high"), fg.col("low"),
                                  fg.col("close"))
    name = "CDLSPINNINGTOP()(open, high, low, close)"
    assert np.array_equal(gen(df).to_numpy(),
                          talib.CDLSPINNINGTOP(df["open"], df["high"],
                                               df["low"],
                                               df["close"]).alias(name),
                          equal_nan=True)


class TestCdllongline:

  def test_cdllongline(self):
    gen = fg.talib.cdllongline(fg.col("open"), fg.col("high"), fg.col("low"),
                               fg.col("close"))
    name = "CDLLONGLINE()(open, high, low, close)"
    assert np.array_equal(gen(df).to_numpy(),
                          talib.CDLLONGLINE(df["open"], df["high"], df["low"],
                                            df["close"]).alias(name),
                          equal_nan=True)


class TestCdlinvertedhammer:

  def test_cdlinvertedhammer(self):
    gen = fg.talib.cdlinvertedhammer(fg.col("open"), fg.col("high"),
                                     fg.col("low"), fg.col("close"))
    name = "CDLINVERTEDHAMMER()(open, high, low, close)"
    assert np.array_equal(gen(df).to_numpy(),
                          talib.CDLINVERTEDHAMMER(df["open"], df["high"],
                                                  df["low"],
                                                  df["close"]).alias(name),
                          equal_nan=True)


class TestCdlxsidegap3methods:

  def test_cdlxsidegap3methods(self):
    gen = fg.talib.cdlxsidegap3methods(fg.col("open"), fg.col("high"),
                                       fg.col("low"), fg.col("close"))
    name = "CDLXSIDEGAP3METHODS()(open, high, low, close)"
    assert np.array_equal(gen(df).to_numpy(),
                          talib.CDLXSIDEGAP3METHODS(df["open"], df["high"],
                                                    df["low"],
                                                    df["close"]).alias(name),
                          equal_nan=True)


class TestCdlengulfing:

  def test_cdlengulfing(self):
    gen = fg.talib.cdlengulfing(fg.col("open"), fg.col("high"), fg.col("low"),
                                fg.col("close"))
    name = "CDLENGULFING()(open, high, low, close)"
    assert np.array_equal(gen(df).to_numpy(),
                          talib.CDLENGULFING(df["open"], df["high"], df["low"],
                                             df["close"]).alias(name),
                          equal_nan=True)


class TestCdlhikkakemod:

  def test_cdlhikkakemod(self):
    gen = fg.talib.cdlhikkakemod(fg.col("open"), fg.col("high"), fg.col("low"),
                                 fg.col("close"))
    name = "CDLHIKKAKEMOD()(open, high, low, close)"
    assert np.array_equal(gen(df).to_numpy(),
                          talib.CDLHIKKAKEMOD(df["open"], df["high"], df["low"],
                                              df["close"]).alias(name),
                          equal_nan=True)


class TestCdlharami:

  def test_cdlharami(self):
    gen = fg.talib.cdlharami(fg.col("open"), fg.col("high"), fg.col("low"),
                             fg.col("close"))
    name = "CDLHARAMI()(open, high, low, close)"
    assert np.array_equal(gen(df).to_numpy(),
                          talib.CDLHARAMI(df["open"], df["high"], df["low"],
                                          df["close"]).alias(name),
                          equal_nan=True)


class TestCdladvanceblock:

  def test_cdladvanceblock(self):
    gen = fg.talib.cdladvanceblock(fg.col("open"), fg.col("high"),
                                   fg.col("low"), fg.col("close"))
    name = "CDLADVANCEBLOCK()(open, high, low, close)"
    assert np.array_equal(gen(df).to_numpy(),
                          talib.CDLADVANCEBLOCK(df["open"], df["high"],
                                                df["low"],
                                                df["close"]).alias(name),
                          equal_nan=True)


class TestCdltasukigap:

  def test_cdltasukigap(self):
    gen = fg.talib.cdltasukigap(fg.col("open"), fg.col("high"), fg.col("low"),
                                fg.col("close"))
    name = "CDLTASUKIGAP()(open, high, low, close)"
    assert np.array_equal(gen(df).to_numpy(),
                          talib.CDLTASUKIGAP(df["open"], df["high"], df["low"],
                                             df["close"]).alias(name),
                          equal_nan=True)


class TestCdlonneck:

  def test_cdlonneck(self):
    gen = fg.talib.cdlonneck(fg.col("open"), fg.col("high"), fg.col("low"),
                             fg.col("close"))
    name = "CDLONNECK()(open, high, low, close)"
    assert np.array_equal(gen(df).to_numpy(),
                          talib.CDLONNECK(df["open"], df["high"], df["low"],
                                          df["close"]).alias(name),
                          equal_nan=True)


class TestCdldojistar:

  def test_cdldojistar(self):
    gen = fg.talib.cdldojistar(fg.col("open"), fg.col("high"), fg.col("low"),
                               fg.col("close"))
    name = "CDLDOJISTAR()(open, high, low, close)"
    assert np.array_equal(gen(df).to_numpy(),
                          talib.CDLDOJISTAR(df["open"], df["high"], df["low"],
                                            df["close"]).alias(name),
                          equal_nan=True)


class TestAd:

  def test_ad(self):
    gen = fg.talib.ad(fg.col("high"), fg.col("low"), fg.col("close"),
                      fg.col("volume"))
    name = "AD()(high, low, close, volume)"
    assert np.array_equal(gen(df).to_numpy(),
                          talib.AD(df["high"], df["low"], df["close"],
                                   df["volume"]).alias(name),
                          equal_nan=True)


class TestCdlsticksandwich:

  def test_cdlsticksandwich(self):
    gen = fg.talib.cdlsticksandwich(fg.col("open"), fg.col("high"),
                                    fg.col("low"), fg.col("close"))
    name = "CDLSTICKSANDWICH()(open, high, low, close)"
    assert np.array_equal(gen(df).to_numpy(),
                          talib.CDLSTICKSANDWICH(df["open"], df["high"],
                                                 df["low"],
                                                 df["close"]).alias(name),
                          equal_nan=True)


class TestCdlshortline:

  def test_cdlshortline(self):
    gen = fg.talib.cdlshortline(fg.col("open"), fg.col("high"), fg.col("low"),
                                fg.col("close"))
    name = "CDLSHORTLINE()(open, high, low, close)"
    assert np.array_equal(gen(df).to_numpy(),
                          talib.CDLSHORTLINE(df["open"], df["high"], df["low"],
                                             df["close"]).alias(name),
                          equal_nan=True)


class TestCdl3outside:

  def test_cdl3outside(self):
    gen = fg.talib.cdl3outside(fg.col("open"), fg.col("high"), fg.col("low"),
                               fg.col("close"))
    name = "CDL3OUTSIDE()(open, high, low, close)"
    assert np.array_equal(gen(df).to_numpy(),
                          talib.CDL3OUTSIDE(df["open"], df["high"], df["low"],
                                            df["close"]).alias(name),
                          equal_nan=True)


class TestCdlkicking:

  def test_cdlkicking(self):
    gen = fg.talib.cdlkicking(fg.col("open"), fg.col("high"), fg.col("low"),
                              fg.col("close"))
    name = "CDLKICKING()(open, high, low, close)"
    assert np.array_equal(gen(df).to_numpy(),
                          talib.CDLKICKING(df["open"], df["high"], df["low"],
                                           df["close"]).alias(name),
                          equal_nan=True)


class TestCdldragonflydoji:

  def test_cdldragonflydoji(self):
    gen = fg.talib.cdldragonflydoji(fg.col("open"), fg.col("high"),
                                    fg.col("low"), fg.col("close"))
    name = "CDLDRAGONFLYDOJI()(open, high, low, close)"
    assert np.array_equal(gen(df).to_numpy(),
                          talib.CDLDRAGONFLYDOJI(df["open"], df["high"],
                                                 df["low"],
                                                 df["close"]).alias(name),
                          equal_nan=True)


class TestCdlhighwave:

  def test_cdlhighwave(self):
    gen = fg.talib.cdlhighwave(fg.col("open"), fg.col("high"), fg.col("low"),
                               fg.col("close"))
    name = "CDLHIGHWAVE()(open, high, low, close)"
    assert np.array_equal(gen(df).to_numpy(),
                          talib.CDLHIGHWAVE(df["open"], df["high"], df["low"],
                                            df["close"]).alias(name),
                          equal_nan=True)


class TestCdlmathold:

  def test_cdlmathold(self):
    gen = fg.talib.cdlmathold(fg.col("open"),
                              fg.col("high"),
                              fg.col("low"),
                              fg.col("close"),
                              penetration=1)
    name = "CDLMATHOLD(1)(open, high, low, close)"
    assert np.array_equal(gen(df).to_numpy(),
                          talib.CDLMATHOLD(df["open"],
                                           df["high"],
                                           df["low"],
                                           df["close"],
                                           penetration=1).alias(name),
                          equal_nan=True)


class TestCdlhikkake:

  def test_cdlhikkake(self):
    gen = fg.talib.cdlhikkake(fg.col("open"), fg.col("high"), fg.col("low"),
                              fg.col("close"))
    name = "CDLHIKKAKE()(open, high, low, close)"
    assert np.array_equal(gen(df).to_numpy(),
                          talib.CDLHIKKAKE(df["open"], df["high"], df["low"],
                                           df["close"]).alias(name),
                          equal_nan=True)


class TestCdldoji:

  def test_cdldoji(self):
    gen = fg.talib.cdldoji(fg.col("open"), fg.col("high"), fg.col("low"),
                           fg.col("close"))
    name = "CDLDOJI()(open, high, low, close)"
    assert np.array_equal(gen(df).to_numpy(),
                          talib.CDLDOJI(df["open"], df["high"], df["low"],
                                        df["close"]).alias(name),
                          equal_nan=True)


class TestCdleveningstar:

  def test_cdleveningstar(self):
    gen = fg.talib.cdleveningstar(fg.col("open"),
                                  fg.col("high"),
                                  fg.col("low"),
                                  fg.col("close"),
                                  penetration=1)
    name = "CDLEVENINGSTAR(1)(open, high, low, close)"
    assert np.array_equal(gen(df).to_numpy(),
                          talib.CDLEVENINGSTAR(df["open"],
                                               df["high"],
                                               df["low"],
                                               df["close"],
                                               penetration=1).alias(name),
                          equal_nan=True)


class TestCdlgapsidesidewhite:

  def test_cdlgapsidesidewhite(self):
    gen = fg.talib.cdlgapsidesidewhite(fg.col("open"), fg.col("high"),
                                       fg.col("low"), fg.col("close"))
    name = "CDLGAPSIDESIDEWHITE()(open, high, low, close)"
    assert np.array_equal(gen(df).to_numpy(),
                          talib.CDLGAPSIDESIDEWHITE(df["open"], df["high"],
                                                    df["low"],
                                                    df["close"]).alias(name),
                          equal_nan=True)


class TestCdltristar:

  def test_cdltristar(self):
    gen = fg.talib.cdltristar(fg.col("open"), fg.col("high"), fg.col("low"),
                              fg.col("close"))
    name = "CDLTRISTAR()(open, high, low, close)"
    assert np.array_equal(gen(df).to_numpy(),
                          talib.CDLTRISTAR(df["open"], df["high"], df["low"],
                                           df["close"]).alias(name),
                          equal_nan=True)


class TestCdlthrusting:

  def test_cdlthrusting(self):
    gen = fg.talib.cdlthrusting(fg.col("open"), fg.col("high"), fg.col("low"),
                                fg.col("close"))
    name = "CDLTHRUSTING()(open, high, low, close)"
    assert np.array_equal(gen(df).to_numpy(),
                          talib.CDLTHRUSTING(df["open"], df["high"], df["low"],
                                             df["close"]).alias(name),
                          equal_nan=True)


class TestCdlshootingstar:

  def test_cdlshootingstar(self):
    gen = fg.talib.cdlshootingstar(fg.col("open"), fg.col("high"),
                                   fg.col("low"), fg.col("close"))
    name = "CDLSHOOTINGSTAR()(open, high, low, close)"
    assert np.array_equal(gen(df).to_numpy(),
                          talib.CDLSHOOTINGSTAR(df["open"], df["high"],
                                                df["low"],
                                                df["close"]).alias(name),
                          equal_nan=True)


class TestCdlbelthold:

  def test_cdlbelthold(self):
    gen = fg.talib.cdlbelthold(fg.col("open"), fg.col("high"), fg.col("low"),
                               fg.col("close"))
    name = "CDLBELTHOLD()(open, high, low, close)"
    assert np.array_equal(gen(df).to_numpy(),
                          talib.CDLBELTHOLD(df["open"], df["high"], df["low"],
                                            df["close"]).alias(name),
                          equal_nan=True)


class TestBop:

  def test_bop(self):
    gen = fg.talib.bop(fg.col("open"), fg.col("high"), fg.col("low"),
                       fg.col("close"))
    name = "BOP()(open, high, low, close)"
    assert np.array_equal(gen(df).to_numpy(),
                          talib.BOP(df["open"], df["high"], df["low"],
                                    df["close"]).alias(name),
                          equal_nan=True)


class TestCdlhammer:

  def test_cdlhammer(self):
    gen = fg.talib.cdlhammer(fg.col("open"), fg.col("high"), fg.col("low"),
                             fg.col("close"))
    name = "CDLHAMMER()(open, high, low, close)"
    assert np.array_equal(gen(df).to_numpy(),
                          talib.CDLHAMMER(df["open"], df["high"], df["low"],
                                          df["close"]).alias(name),
                          equal_nan=True)


class TestCdlrisefall3methods:

  def test_cdlrisefall3methods(self):
    gen = fg.talib.cdlrisefall3methods(fg.col("open"), fg.col("high"),
                                       fg.col("low"), fg.col("close"))
    name = "CDLRISEFALL3METHODS()(open, high, low, close)"
    assert np.array_equal(gen(df).to_numpy(),
                          talib.CDLRISEFALL3METHODS(df["open"], df["high"],
                                                    df["low"],
                                                    df["close"]).alias(name),
                          equal_nan=True)


class TestCdlhangingman:

  def test_cdlhangingman(self):
    gen = fg.talib.cdlhangingman(fg.col("open"), fg.col("high"), fg.col("low"),
                                 fg.col("close"))
    name = "CDLHANGINGMAN()(open, high, low, close)"
    assert np.array_equal(gen(df).to_numpy(),
                          talib.CDLHANGINGMAN(df["open"], df["high"], df["low"],
                                              df["close"]).alias(name),
                          equal_nan=True)


class TestCdl3whitesoldiers:

  def test_cdl3whitesoldiers(self):
    gen = fg.talib.cdl3whitesoldiers(fg.col("open"), fg.col("high"),
                                     fg.col("low"), fg.col("close"))
    name = "CDL3WHITESOLDIERS()(open, high, low, close)"
    assert np.array_equal(gen(df).to_numpy(),
                          talib.CDL3WHITESOLDIERS(df["open"], df["high"],
                                                  df["low"],
                                                  df["close"]).alias(name),
                          equal_nan=True)


class TestCdleveningdojistar:

  def test_cdleveningdojistar(self):
    gen = fg.talib.cdleveningdojistar(fg.col("open"),
                                      fg.col("high"),
                                      fg.col("low"),
                                      fg.col("close"),
                                      penetration=1)
    name = "CDLEVENINGDOJISTAR(1)(open, high, low, close)"
    assert np.array_equal(gen(df).to_numpy(),
                          talib.CDLEVENINGDOJISTAR(df["open"],
                                                   df["high"],
                                                   df["low"],
                                                   df["close"],
                                                   penetration=1).alias(name),
                          equal_nan=True)


class TestCdltakuri:

  def test_cdltakuri(self):
    gen = fg.talib.cdltakuri(fg.col("open"), fg.col("high"), fg.col("low"),
                             fg.col("close"))
    name = "CDLTAKURI()(open, high, low, close)"
    assert np.array_equal(gen(df).to_numpy(),
                          talib.CDLTAKURI(df["open"], df["high"], df["low"],
                                          df["close"]).alias(name),
                          equal_nan=True)


class TestCdlharamicross:

  def test_cdlharamicross(self):
    gen = fg.talib.cdlharamicross(fg.col("open"), fg.col("high"), fg.col("low"),
                                  fg.col("close"))
    name = "CDLHARAMICROSS()(open, high, low, close)"
    assert np.array_equal(gen(df).to_numpy(),
                          talib.CDLHARAMICROSS(df["open"], df["high"],
                                               df["low"],
                                               df["close"]).alias(name),
                          equal_nan=True)


class TestCdl3inside:

  def test_cdl3inside(self):
    gen = fg.talib.cdl3inside(fg.col("open"), fg.col("high"), fg.col("low"),
                              fg.col("close"))
    name = "CDL3INSIDE()(open, high, low, close)"
    assert np.array_equal(gen(df).to_numpy(),
                          talib.CDL3INSIDE(df["open"], df["high"], df["low"],
                                           df["close"]).alias(name),
                          equal_nan=True)


class TestCdlupsidegap2crows:

  def test_cdlupsidegap2crows(self):
    gen = fg.talib.cdlupsidegap2crows(fg.col("open"), fg.col("high"),
                                      fg.col("low"), fg.col("close"))
    name = "CDLUPSIDEGAP2CROWS()(open, high, low, close)"
    assert np.array_equal(gen(df).to_numpy(),
                          talib.CDLUPSIDEGAP2CROWS(df["open"], df["high"],
                                                   df["low"],
                                                   df["close"]).alias(name),
                          equal_nan=True)


class TestCdlconcealbabyswall:

  def test_cdlconcealbabyswall(self):
    gen = fg.talib.cdlconcealbabyswall(fg.col("open"), fg.col("high"),
                                       fg.col("low"), fg.col("close"))
    name = "CDLCONCEALBABYSWALL()(open, high, low, close)"
    assert np.array_equal(gen(df).to_numpy(),
                          talib.CDLCONCEALBABYSWALL(df["open"], df["high"],
                                                    df["low"],
                                                    df["close"]).alias(name),
                          equal_nan=True)


class TestCdlmatchinglow:

  def test_cdlmatchinglow(self):
    gen = fg.talib.cdlmatchinglow(fg.col("open"), fg.col("high"), fg.col("low"),
                                  fg.col("close"))
    name = "CDLMATCHINGLOW()(open, high, low, close)"
    assert np.array_equal(gen(df).to_numpy(),
                          talib.CDLMATCHINGLOW(df["open"], df["high"],
                                               df["low"],
                                               df["close"]).alias(name),
                          equal_nan=True)


class TestCdlclosingmarubozu:

  def test_cdlclosingmarubozu(self):
    gen = fg.talib.cdlclosingmarubozu(fg.col("open"), fg.col("high"),
                                      fg.col("low"), fg.col("close"))
    name = "CDLCLOSINGMARUBOZU()(open, high, low, close)"
    assert np.array_equal(gen(df).to_numpy(),
                          talib.CDLCLOSINGMARUBOZU(df["open"], df["high"],
                                                   df["low"],
                                                   df["close"]).alias(name),
                          equal_nan=True)


class TestCdlkickingbylength:

  def test_cdlkickingbylength(self):
    gen = fg.talib.cdlkickingbylength(fg.col("open"), fg.col("high"),
                                      fg.col("low"), fg.col("close"))
    name = "CDLKICKINGBYLENGTH()(open, high, low, close)"
    assert np.array_equal(gen(df).to_numpy(),
                          talib.CDLKICKINGBYLENGTH(df["open"], df["high"],
                                                   df["low"],
                                                   df["close"]).alias(name),
                          equal_nan=True)


class TestCdlmarubozu:

  def test_cdlmarubozu(self):
    gen = fg.talib.cdlmarubozu(fg.col("open"), fg.col("high"), fg.col("low"),
                               fg.col("close"))
    name = "CDLMARUBOZU()(open, high, low, close)"
    assert np.array_equal(gen(df).to_numpy(),
                          talib.CDLMARUBOZU(df["open"], df["high"], df["low"],
                                            df["close"]).alias(name),
                          equal_nan=True)


class TestSarext:

  def test_sarext(self):
    gen = fg.talib.sarext(fg.col("high"),
                          fg.col("low"),
                          startvalue=1,
                          offsetonreverse=1,
                          accelerationinitlong=1,
                          accelerationlong=1,
                          accelerationmaxlong=1,
                          accelerationinitshort=1,
                          accelerationshort=1,
                          accelerationmaxshort=1)
    name = "SAREXT(1, 1, 1, 1, 1, 1, 1, 1)(high, low)"
    assert np.array_equal(gen(df).to_numpy(),
                          talib.SAREXT(df["high"],
                                       df["low"],
                                       startvalue=1,
                                       offsetonreverse=1,
                                       accelerationinitlong=1,
                                       accelerationlong=1,
                                       accelerationmaxlong=1,
                                       accelerationinitshort=1,
                                       accelerationshort=1,
                                       accelerationmaxshort=1).alias(name),
                          equal_nan=True)


class TestMinus_dm:

  def test_minus_dm(self):
    gen = fg.talib.minus_dm(fg.col("low"), fg.col("high"), timeperiod=3)
    name = "MINUS_DM(3)(low, high)"
    assert np.array_equal(gen(df).to_numpy(),
                          talib.MINUS_DM(df["low"], df["high"],
                                         timeperiod=3).alias(name),
                          equal_nan=True)


class TestBeta:

  def test_beta(self):
    gen = fg.talib.beta(fg.col("high"), fg.col("low"), timeperiod=3)
    name = "BETA(3)(high, low)"
    assert np.array_equal(gen(df).to_numpy(),
                          talib.BETA(df["high"], df["low"],
                                     timeperiod=3).alias(name),
                          equal_nan=True)


class TestCorrel:

  def test_correl(self):
    gen = fg.talib.correl(fg.col("high"), fg.col("low"), timeperiod=3)
    name = "CORREL(3)(high, low)"
    assert np.array_equal(gen(df).to_numpy(),
                          talib.CORREL(df["high"], df["low"],
                                       timeperiod=3).alias(name),
                          equal_nan=True)


class TestAroon_0:

  def test_aroon_0(self):
    gen = fg.talib.aroon_0(fg.col("high"), fg.col("low"), timeperiod=3)
    name = "AROON_0(3)(high, low)"
    assert np.array_equal(gen(df).to_numpy(),
                          talib.AROON(df["high"], df["low"],
                                      timeperiod=3)[0].alias(name),
                          equal_nan=True)


class TestAroon_1:

  def test_aroon_1(self):
    gen = fg.talib.aroon_1(fg.col("high"), fg.col("low"), timeperiod=3)
    name = "AROON_1(3)(high, low)"
    assert np.array_equal(gen(df).to_numpy(),
                          talib.AROON(df["high"], df["low"],
                                      timeperiod=3)[1].alias(name),
                          equal_nan=True)


class TestPlus_dm:

  def test_plus_dm(self):
    gen = fg.talib.plus_dm(fg.col("high"), fg.col("low"), timeperiod=3)
    name = "PLUS_DM(3)(high, low)"
    assert np.array_equal(gen(df).to_numpy(),
                          talib.PLUS_DM(df["high"], df["low"],
                                        timeperiod=3).alias(name),
                          equal_nan=True)


class TestMidprice:

  def test_midprice(self):
    gen = fg.talib.midprice(fg.col("high"), fg.col("low"), timeperiod=3)
    name = "MIDPRICE(3)(high, low)"
    assert np.array_equal(gen(df).to_numpy(),
                          talib.MIDPRICE(df["high"], df["low"],
                                         timeperiod=3).alias(name),
                          equal_nan=True)


class TestAroonosc:

  def test_aroonosc(self):
    gen = fg.talib.aroonosc(fg.col("high"), fg.col("low"), timeperiod=3)
    name = "AROONOSC(3)(high, low)"
    assert np.array_equal(gen(df).to_numpy(),
                          talib.AROONOSC(df["high"], df["low"],
                                         timeperiod=3).alias(name),
                          equal_nan=True)


class TestSar:

  def test_sar(self):
    gen = fg.talib.sar(fg.col("high"), fg.col("low"), acceleration=1, maximum=1)
    name = "SAR(1, 1)(high, low)"
    assert np.array_equal(gen(df).to_numpy(),
                          talib.SAR(df["high"],
                                    df["low"],
                                    acceleration=1,
                                    maximum=1).alias(name),
                          equal_nan=True)


class TestObv:

  def test_obv(self):
    gen = fg.talib.obv(fg.col("close"), fg.col("volume"))
    name = "OBV()(close, volume)"
    assert np.array_equal(gen(df).to_numpy(),
                          talib.OBV(df["close"], df["volume"]).alias(name),
                          equal_nan=True)
