import re
from dataclasses import dataclass


@dataclass
class FeatureArg:
  name: str
  type: str

  @property
  def arg_def_component(self) -> str:
    return f"{self.name}: {self.type}"

  @classmethod
  def from_str(cls, arg_str: str) -> "FeatureArg":
    name, type = arg_str.split(":")
    return cls(name.strip(), type.strip())


@dataclass
class TalibFeature:
  file_content: str
  kind: str
  path: str

  name_regex = re.compile(r".*?class (\w+)\(.*")
  init_arg_regex = re.compile(r".*?def __init__\(self,(.*?)\):.*",
                              re.MULTILINE | re.DOTALL)

  @property
  def name(self) -> str:
    for line in self.file_content.split("\n"):
      if "class" in line and self.kind.capitalize() in line:
        return self.name_regex.match(line).group(1).replace("Feature", "")

  @property
  def init_args(self) -> list[FeatureArg]:
    init_arg_component = self.init_arg_regex.match(
        self.file_content).group(1).replace(" ", "").replace("\n", "")
    return [FeatureArg.from_str(s) for s in init_arg_component.split(",")]

  @property
  def file_name(self) -> str:
    return self.path.split("/")[-1].replace(".py", "")

  @staticmethod
  def read(path: str) -> list["TalibFeature"]:
    kind = path.split("/")[2]

    with open(path, "r") as f:
      content = f.read()
      contents = content.split("\n")
      class_indexes = [i for i, c in enumerate(contents) if "class" in c]

      class_decls = []
      for i, class_index in enumerate(class_indexes):
        if i == len(class_indexes) - 1:
          class_decls.append("\n".join(contents[class_index:]))
        else:
          class_decls.append("\n".join(contents[class_index:class_indexes[i +
                                                                          1]]))

      return [TalibFeature(c, kind, path) for c in class_decls]
