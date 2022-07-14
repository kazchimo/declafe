from typing import TYPE_CHECKING

if TYPE_CHECKING:
  from declafe import FeatureGen


class OpsMixin:

  def __init__(self):
    from declafe.ConstFeature import ConstFeature
    from declafe.binary.BiComposeFeature import BiComposeFeature
    self.C = ConstFeature
    self.BC = BiComposeFeature

  def __eq__(self: "FeatureGen", other):
    from declafe.binary import EqualFeature, BiComposeFeature

    return BiComposeFeature.make(
        left=self, right=self.C.conv(other), to=EqualFeature)

  def __ne__(self: "FeatureGen", other):
    return (self == other).flip_bool()

  def __add__(self: "FeatureGen", other):
    from declafe.binary import AddFeature
    return self.BC.make(left=self, right=other, to=AddFeature)

  def __sub__(self: "FeatureGen", other):
    from declafe.binary import SubFeature

    return self.BC.make(self, self.C.conv(other), SubFeature)

  def __mul__(self: "FeatureGen", other):
    from declafe.binary import ProductFeature

    return self.BC.make(self, self.C.conv(other), ProductFeature)

  def __mod__(self: "FeatureGen", other):
    from declafe.binary import ModFeature

    return self.BC.make(self, self.C.conv(other), ModFeature)

  def __truediv__(self: "FeatureGen", other: "FeatureGen") -> "FeatureGen":
    from declafe.binary import DivideFeature

    return self.BC.make(self, self.C.conv(other), DivideFeature)

  def __gt__(self: "FeatureGen", other):
    from declafe.binary import IsGreaterFeature

    return self.BC.make(self, self.C.conv(other), IsGreaterFeature)

  def __lt__(self: "FeatureGen", other):
    from declafe.binary import IsLessFeature

    return self.BC.make(self, self.C.conv(other), IsLessFeature)

  def __ge__(self: "FeatureGen", other):
    from declafe.binary import GEFeature

    return self.BC.make(self, self.C.conv(other), GEFeature)

  def __le__(self: "FeatureGen", other):
    from declafe.binary import LEFeature

    return self.BC.make(self, self.C.conv(other), LEFeature)
