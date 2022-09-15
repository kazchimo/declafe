import pandas as pd

from declafe import col

test_df = pd.DataFrame({
    "b1": [True, False, True, False],
    "b2": [True, True, False, False],
})

b1 = col("b1")
b2 = col("b2")


class TestEq:

  def test_eq(self):
    assert (b1 == b2).gen(test_df).equals(pd.Series([True, False, False, True]))

  def test_with_constant(self):
    assert (b1 == True).gen(test_df).equals(
        pd.Series([True, False, True, False]))
    assert (b1 == False).gen(test_df).equals(
        pd.Series([False, True, False, True]))


class TestNe:

  def test_ne(self):
    assert (b1 != b2).gen(test_df).equals(pd.Series([False, True, True, False]))

  def test_with_constant(self):
    assert (b1 != True).gen(test_df).equals(
        pd.Series([False, True, False, True]))
    assert (b1 != False).gen(test_df).equals(
        pd.Series([True, False, True, False]))


class TestAdd:

  def test_add(self):
    df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    assert (col("a") + col("b")).gen(df).equals(pd.Series([5, 7, 9]))

  def test_with_const(self):
    df = pd.DataFrame({"a": [1, 2, 3]})
    assert (col("a") + 1).gen(df).equals(pd.Series([2, 3, 4]))


class TestSub:

  def test_sub(self):
    df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    assert (col("a") - col("b")).gen(df).equals(pd.Series([-3, -3, -3]))

  def test_with_const(self):
    df = pd.DataFrame({"a": [1, 2, 3]})
    assert (col("a") - 1).gen(df).equals(pd.Series([0, 1, 2]))


class TestMul:

  def test_mul(self):
    df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    assert (col("a") * col("b")).gen(df).equals(pd.Series([4, 10, 18]))

  def test_with_const(self):
    df = pd.DataFrame({"a": [1, 2, 3]})
    assert (col("a") * 2).gen(df).equals(pd.Series([2, 4, 6]))


class TestMod:

  def test_mod(self):
    df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    assert (col("a") % col("b")).gen(df).equals(pd.Series([1, 2, 3]))

  def test_with_const(self):
    df = pd.DataFrame({"a": [1, 2, 3]})
    assert (col("a") % 2).gen(df).equals(pd.Series([1, 0, 1]))


class TestTrueDiv:

  def test_true_div(self):
    df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    assert (col("a") / col("b")).gen(df).equals(pd.Series([0.25, 0.4, 0.5]))

  def test_with_const(self):
    df = pd.DataFrame({"a": [1, 2, 3]})
    assert (col("a") / 2).gen(df).equals(pd.Series([0.5, 1, 1.5]))


class TestGt:

  def test_gt(self):
    df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    assert (col("a") > col("b")).gen(df).equals(pd.Series([False, False,
                                                           False]))

  def test_with_const(self):
    df = pd.DataFrame({"a": [1, 2, 3]})
    assert (col("a") > 2).gen(df).equals(pd.Series([False, False, True]))


class TestLt:

  def test_lt(self):
    df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    assert (col("a") < col("b")).gen(df).equals(pd.Series([True, True, True]))

  def test_with_const(self):
    df = pd.DataFrame({"a": [1, 2, 3]})
    assert (col("a") < 2).gen(df).equals(pd.Series([True, False, False]))


class TestGe:

  def test_ge(self):
    df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    assert (col("a") >= col("b")).gen(df).equals(
        pd.Series([False, False, False]))

  def test_with_const(self):
    df = pd.DataFrame({"a": [1, 2, 3]})
    assert (col("a") >= 2).gen(df).equals(pd.Series([False, True, True]))


class TestLe:

  def test_le(self):
    df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    assert (col("a") <= col("b")).gen(df).equals(pd.Series([True, True, True]))

  def test_with_const(self):
    df = pd.DataFrame({"a": [1, 2, 3]})
    assert (col("a") <= 2).gen(df).equals(pd.Series([True, True, False]))


class TestAnd:

  def test_and(self):
    assert (b1 & b2).gen(test_df).equals(pd.Series([True, False, False, False]))


class TestOr:

  def test_or(self):
    assert (b1 | b2).gen(test_df).equals(pd.Series([True, True, True, False]))
