import re

from gen.services.talib_constructor_def import TalibConstructorDef


class TalibConstructorTests:

  def __init__(self, chain_defs: list[TalibConstructorDef]):
    self.chain_defs = chain_defs

  @property
  def file_content(self) -> str:
    tests = '\n'.join(
        [self._test_content(chain_def) for chain_def in self.chain_defs])

    return f"""\
import talib
import polars as pl
import declafe.pl.feature_gen as fg
import numpy as np

df = pl.DataFrame({{
      "close": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
      "open": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
      "high": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
      "low": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
      "volume": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    }})

{tests}
"""

  def _test_content(self, chain_def: TalibConstructorDef) -> str:
    idx_component = f"[{chain_def.talib_method_idx}]" if chain_def.talib_method_idx is not None else ""
    arg_component = ", ".join([
        arg.as_pass_component(arg.test_value())
        for idx, arg in enumerate(chain_def.args)
    ])
    arg_names = ", ".join(
        [a.test_value_name() for idx, a in enumerate(chain_def.additionl_args)])
    df_arg_component = ", ".join([
        arg.as_pass_component(arg.test_df_value())
        for idx, arg in enumerate(chain_def.args)
    ])
    primary_args = ", ".join([a.name for a in chain_def.primary_args])

    return f"""\
class Test{chain_def.def_name.capitalize()}:
  def test_{chain_def.def_name}(self):
    gen = fg.talib.{chain_def.def_name}({arg_component})
    name = "{chain_def.def_name.upper()}({arg_names})({primary_args})"
    assert np.array_equal(gen(df).to_numpy(), 
      talib.{chain_def.talib_method_name}({df_arg_component}){idx_component}.alias(name),
      equal_nan=True
    )
"""

  def write(self):
    with open("tests/pl/feature_gen/test_talib_constructor.py", "w") as f:
      f.write(self.file_content)


def main():
  def_regex = re.compile(r'def\s+(\w+)\((.*?)\) -> "FeatureGen":',
                         re.MULTILINE | re.DOTALL)
  with open("pl/feature_gen/talib_constructor.py", "r") as f:
    chain_defs = [
        TalibConstructorDef(l[0], l[1].replace(" ", "").replace("\n", ""))
        for l in def_regex.findall("\n".join(f.read().split("\n")[8:]))
    ]

  chain_tests = TalibConstructorTests(chain_defs)
  chain_tests.write()


if __name__ == "__main__":
  main()
