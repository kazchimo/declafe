from time import time

import numpy as np
import pandas as pd

from declafe import col


def main():
  arr = np.random.random(1000_000)
  df = pd.DataFrame({"a": arr})
  f = col("a").moving_max(1000)

  print("without numba")
  start = time()
  f.generate(df)
  end = time()
  print("Elapsed time:", end - start)

  print("with numba")
  start = time()
  f.enable_numba().generate(df)
  end = time()
  print("Elapsed time:", end - start)


if __name__ == "__main__":
  main()
