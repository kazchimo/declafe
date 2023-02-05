import re
from dataclasses import dataclass
from typing import Optional
from textwrap import indent


@dataclass
class Arg:
  name: str
  type: str
  default: Optional[str] = None

  @staticmethod
  def from_str(s: str) -> 'Arg':
    name, other = s.split(':')

    if '=' in other and ("..." not in other):
      type, default = other.split('=')
    elif '...' in other:
      type = other.replace('...', '').replace("=", '')
      default = None
    else:
      type = other
      default = None

    return Arg(name.strip(), type.strip(), default.strip() if default else None)

  def is_type(self, type_: str) -> bool:
    return self.type == type_

  def to_arg_component(self) -> str:
    if self.default:
      return f'{self.name}: {self.type}={self.default}'
    else:
      return f"{self.name}: {self.type}"

  def to_init_component(self) -> str:
    return f"self.{self.name} = {self.name}"


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


class TalibFeatureFile:

  def __init__(self, talib_def: TalibDef):
    self.talib_def = talib_def

  def _init_component(self) -> str:
    additionals = (", " + ', '.join([ a.to_arg_component() for a in self.talib_def.additional_args ])) \
      if self.talib_def.additional_args \
      else ''
    additional_inits = "\n".join([a.to_init_component() for a in self.talib_def.additional_args]) \
      if self.talib_def.additional_args \
      else ''

    if self.talib_def.feature_kind_num == 1:
      return f"""def __init__(self, column: ColLike{additionals}):
  super().__init__(column)
{indent(additional_inits, "  ")}
  """
    elif self.talib_def.feature_kind_num == 2:
      return f"""def __init__(self, left: ColLike, right: ColLike{additionals}):
  super().__init__(left, right)
{indent(additional_inits, "  ")}
  """
    elif self.talib_def.feature_kind_num == 3:
      return f"""def __init__(self, col1: ColLike, col2: ColLike, col3: ColLike{additionals}):
  super().__init__(col1, col2, col3)
{indent(additional_inits, "  ")}
  """
    elif self.talib_def.feature_kind_num == 4:
      return f"""def __init__(self, col1: ColLike, col2: ColLike, col3: ColLike, col4: ColLike{additionals}):
  super().__init__(col1, col2, col3, col4)
{indent(additional_inits, "  ")}
  """
    else:
      raise ValueError("Invalid number of feature kinds")

  @property
  def _import_base_class_component(self) -> str:
    kind = self.talib_def.feature_kind
    cap_kind = self.talib_def.cap_feature_kind

    return f"from pl.feature_gen.{kind}.{kind}_feature import {cap_kind}Feature"

  def _expr_component(self, i: Optional[int] = None) -> str:
    idx_component = f"[{i}]" if i is not None else ""
    additionals = ",\n".join([f"{a.name}=self.{a.name}" for a in self.talib_def.additional_args]) \
      if self.talib_def.additional_args \
      else ''

    if self.talib_def.feature_kind_num == 1:
      return f"""\
def _unary_expr(self, orig_col: pl.Expr) -> pl.Expr:
  return orig_col.map(lambda s: talib.{self.talib_def.name}(
    s,
{indent(additionals, "    ")}
  ){idx_component})
  """
    elif self.talib_def.feature_kind_num == 2:
      return f"""\
def _binary_expr(self, left: pl.Expr, right: pl.Expr) -> pl.Expr:
  return pl.struct([left, right]).map(lambda s: talib.{self.talib_def.name}(
    s[f'{{self.left.feature_name}}'],
    s[f'{{self.right.feature_name}}'],
{indent(additionals, "    ")}
  ){idx_component})
"""
    elif self.talib_def.feature_kind_num == 3:
      return f"""\
def _tri_expr(self, col1: pl.Expr, col2: pl.Expr, col3: pl.Expr) -> pl.Expr:
  return pl.struct([col1, col2, col3]).map(lambda s: talib.{self.talib_def.name}(
    s[f'{{self.col1.feature_name}}'],
    s[f'{{self.col2.feature_name}}'],
    s[f'{{self.col3.feature_name}}'],
{indent(additionals, "    ")}
  ){idx_component})
"""
    elif self.talib_def.feature_kind_num == 4:
      return f"""\
def _quadri_expr(self, col1: pl.Expr, col2: pl.Expr, col3: pl.Expr, col4: pl.Expr) -> pl.Expr:
  return pl.struct([col1, col2, col3, col4]).map(lambda s: talib.{self.talib_def.name}(
    s[f'{{self.col1.feature_name}}'],
    s[f'{{self.col2.feature_name}}'],
    s[f'{{self.col3.feature_name}}'],
    s[f'{{self.col4.feature_name}}'],
{indent(additionals, "    ")}
  ){idx_component})
"""
    else:
      raise ValueError("Invalid number of feature kinds")

  def _feature_name_component(self, i: Optional[int] = None) -> str:
    idx_component = f"_{i}" if i is not None else ""
    additionals = ", ".join(
        [f"{{self.{a.name}}}" for a in self.talib_def.additional_args])

    if self.talib_def.feature_kind_num == 1:
      arg_component = f"{{self.column}}"
    elif self.talib_def.feature_kind_num == 2:
      arg_component = f"{{self.left}}, {{self.right}}"
    elif self.talib_def.feature_kind_num == 3:
      arg_component = f"{{self.col1}}, {{self.col2}}, {{self.col3}}"
    elif self.talib_def.feature_kind_num == 4:
      arg_component = f"{{self.col1}}, {{self.col2}}, {{self.col3}}, {{self.col4}}"
    else:
      raise ValueError("Invalid number of feature kinds")

    return f"""\
def _feature_names(self) -> list[str]:
  return [
    f'{self.talib_def.name}{idx_component}({additionals})({arg_component})'
  ]
    """

  @property
  def file_content(self) -> str:

    def content(i: Optional[int] = None):
      name_idx = f"{self.talib_def.name}_{i}" if i is not None else self.talib_def.name

      return f"""\
      
class {name_idx}Feature({self.talib_def.cap_feature_kind}Feature):
{indent(self._init_component(), "  ")}

{indent(self._expr_component(i), "  ")}

{indent(self._feature_name_component(i), "  ")}
"""

    import_component = f"""\
import polars as pl
from pl.feature_gen.types import ColLike
import talib
{self._import_base_class_component}
"""

    if self.talib_def.return_num == 1:
      return import_component + content()
    else:
      return import_component + "\n\n".join(
          [content(i) for i in range(self.talib_def.return_num)])

  @property
  def file_path(self) -> str:
    return f"pl/feature_gen/{self.talib_def.feature_kind}/talib/{self.talib_def.name.lower()}_feature.py"

  def write(self):
    with open(self.file_path, "w") as f:
      f.write(self.file_content)


with open("typings/talib/__init__.pyi", "r") as f:
  file = f.read()

pl_decls = [
    TalibDef(l) for l in file.split("\n") if "pl.Series" in l and "def" in l
]

for talib_def in pl_decls:
  TalibFeatureFile(talib_def).write()
