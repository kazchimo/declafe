from dataclasses import dataclass
from typing import Optional


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

  def to_arg_component(self, tpe: Optional[str] = None) -> str:
    tpe = tpe or self.type

    if self.default:
      return f'{self.name}: {tpe}={self.default}'
    else:
      return f"{self.name}: {tpe}"

  def to_init_component(self) -> str:
    return f"self.{self.name} = {self.name}"
