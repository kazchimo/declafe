import re
from dataclasses import dataclass
from typing import Optional


@dataclass
class Arg:
  name: str
  type: str

  @staticmethod
  def read(line: str) -> "Arg":
    name, type = line.split(":")
    return Arg(name.strip(), type.strip())

  def as_pass_component(self, value: str) -> str:
    return f"{self.name}={value}"

  @property
  def test_value(self) -> str:
    if "type" in self.name:
      return "1"
    elif "period" in self.name:
      return "3"
    elif "fastlimit" in self.name:
      return "0.5"
    elif "slowlimit" in self.name:
      return "0.05"
    else:
      return "1"


@dataclass
class TalibChainDef:
  def_name: str
  _args: str

  _talib_multi_multi_methods_regex = re.compile(r"(.*)_(\d)")

  @property
  def args(self) -> list[Arg]:
    return [Arg.read(a) for a in self._args.split(",")[1:]]

  @property
  def talib_method_name(self) -> str:
    if self._talib_multi_multi_methods_regex.match(self.def_name):
      return self._talib_multi_multi_methods_regex.match(
          self.def_name).group(1).upper()
    else:
      return self.def_name.upper()

  @property
  def talib_method_idx(self) -> Optional[int]:
    if self._talib_multi_multi_methods_regex.match(self.def_name):
      return int(self.def_name[-1])
    else:
      return None
