import numpy as np
import pandas as pd

from declafe import col, c
from declafe.feature_gen.tri.TriFeature import TriFeature

test_df = pd.DataFrame({
    "a": list(range(1, 1001)),
    "b": list(range(1001, 2001))
})

a = col("a")
b = col("b")


class Add3Feature(TriFeature):

  def trigen(self, col1: np.ndarray, col2: np.ndarray,
             col3: np.ndarray) -> np.ndarray:
    return col1 + col2 + col3

  def _feature_name(self) -> str:
    return f"{self.col1} + {self.col2} + {self.col3}"


class TestWithConst:

  def test_gen_using_const(self):
    df = test_df.copy()
    f = Add3Feature(a, b, c(1)).to_features
    result = f.set_features(df)

    assert result["a + b + 1"].equals(df["a"] + df["b"] + 1)
