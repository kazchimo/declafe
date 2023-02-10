import re
from dataclasses import dataclass

from gen.services.arg import Arg


@dataclass
class TalibDef:
  decl_line: str

  name_regex = re.compile(r"def (\w+)\(.*")
  arg_regex = re.compile(r"def \w+\((.*)\).*")
  return_regex = re.compile(r"def \w+\(.*\)\s*->\s*(.+):.*")

  @property
  def name(self) -> str:
    return self.name_regex.match(self.decl_line).group(1)

  @property
  def return_num(self) -> int:
    return self.return_regex.match(self.decl_line).group(1).count("pl.Series")

  @property
  def args(self) -> list[Arg]:
    arg_component = self.arg_regex.match(self.decl_line).group(1)
    return [Arg.from_str(arg.strip()) for arg in arg_component.split(",")]

  @property
  def feature_kind_num(self) -> int:
    return len([arg for arg in self.args if arg.is_type("pl.Series")])

  @property
  def feature_kind(self) -> str:
    if self.feature_kind_num == 1:
      return "unary"
    elif self.feature_kind_num == 2:
      return "binary"
    elif self.feature_kind_num == 3:
      return "tri"
    elif self.feature_kind_num == 4:
      return "quadri"
    else:
      raise ValueError("Invalid number of feature kinds")

  @property
  def cap_feature_kind(self) -> str:
    return self.feature_kind.capitalize()

  @property
  def additional_args(self) -> list[Arg]:
    return [arg for arg in self.args if not arg.is_type("pl.Series")]

  @property
  def primary_args(self) -> list[Arg]:
    return [arg for arg in self.args if arg.is_type("pl.Series")]
