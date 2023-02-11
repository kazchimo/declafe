from typing import Optional
from textwrap import indent

from gen.services.talib_def import TalibDef


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
    primary_args = ", ".join(
        [a.to_arg_component("ColLike") for a in self.talib_def.primary_args])
    primary_args_pass = ", ".join([a.name for a in self.talib_def.primary_args])

    return f"""def __init__(self, {primary_args}{additionals}):
  super().__init__({primary_args_pass})
{indent(additional_inits, "  ")}
  """

  @property
  def _import_base_class_component(self) -> str:
    kind = self.talib_def.feature_kind
    cap_kind = self.talib_def.cap_feature_kind

    return f"from declafe.pl.feature_gen.{kind}.{kind}_feature import {cap_kind}Feature"

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
  return cast(pl.Expr, pl.struct([left, right])).map(lambda s: talib.{self.talib_def.name}(
    s.struct.field(self.left_feature.feature_name),
    s.struct.field(self.right_feature.feature_name),
{indent(additionals, "    ")}
  ){idx_component})
"""
    elif self.talib_def.feature_kind_num == 3:
      return f"""\
def _tri_expr(self, col1: pl.Expr, col2: pl.Expr, col3: pl.Expr) -> pl.Expr:
  return cast(pl.Expr, pl.struct([col1, col2, col3])).map(lambda s: talib.{self.talib_def.name}(
    s.struct.field(self.col1_feature.feature_name),
    s.struct.field(self.col2_feature.feature_name),
    s.struct.field(self.col3_feature.feature_name),
{indent(additionals, "    ")}
  ){idx_component})
"""
    elif self.talib_def.feature_kind_num == 4:
      return f"""\
def _quadri_expr(self, col1: pl.Expr, col2: pl.Expr, col3: pl.Expr, col4: pl.Expr) -> pl.Expr:
  return cast(pl.Expr, pl.struct([col1, col2, col3, col4])).map(lambda s: talib.{self.talib_def.name}(
    s.struct.field(self.col1_feature.feature_name),
    s.struct.field(self.col2_feature.feature_name),
    s.struct.field(self.col3_feature.feature_name),
    s.struct.field(self.col4_feature.feature_name),
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
      arg_component = f"{{self.col_feature.feature_name}}"
    elif self.talib_def.feature_kind_num == 2:
      arg_component = f"{{self.left_feature.feature_name}}, {{self.right_feature.feature_name}}"
    elif self.talib_def.feature_kind_num == 3:
      arg_component = f"{{self.col1_feature.feature_name}}, {{self.col2_feature.feature_name}}, " \
                      f"{{self.col3_feature.feature_name}}"
    elif self.talib_def.feature_kind_num == 4:
      arg_component = f"{{self.col1_feature.feature_name}}, {{self.col2_feature.feature_name}}, {{self.col3_feature.feature_name}}, {{self.col4_feature.feature_name}}"
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
from declafe.pl.feature_gen.types import ColLike
import talib
{"from typing import cast" if self.talib_def.feature_kind_num > 1 else ""}

{self._import_base_class_component}
"""

    if self.talib_def.return_num == 1:
      return import_component + content()
    else:
      return import_component + "\n\n".join(
          [content(i) for i in range(self.talib_def.return_num)])

  @property
  def file_path(self) -> str:
    return f"declafe/pl/feature_gen/{self.talib_def.feature_kind}/talib/{self.talib_def.name.lower()}_feature.py"

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
