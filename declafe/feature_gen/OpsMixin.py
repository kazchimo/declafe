from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
  from declafe import FeatureGen


class OpsMixin:

  @staticmethod
  def _bc():
    from declafe.binary.BiComposeFeature import BiComposeFeature
    return BiComposeFeature

  @staticmethod
  def _conv(a: Any):
    from declafe.ConstFeature import ConstFeature
    return ConstFeature.conv(a)

  def __eq__(self: "FeatureGen", other):
    from declafe.binary import EqualFeature, BiComposeFeature

    return BiComposeFeature.make(
        left=self, right=self._conv(other), to=EqualFeature)

  def __ne__(self: "FeatureGen", other):
    return (self == other).flip_bool()

  def __add__(self: "FeatureGen", other):
    from declafe.binary import AddFeature
    return self._bc().make(left=self, right=self._conv(other), to=AddFeature)

  def __sub__(self: "FeatureGen", other):
    from declafe.binary import SubFeature

    return self._bc().make(self, self._conv(other), SubFeature)

  def __mul__(self: "FeatureGen", other):
    from declafe.binary import ProductFeature

    return self._bc().make(self, self._conv(other), ProductFeature)

  def __mod__(self: "FeatureGen", other):
    from declafe.binary import ModFeature

    return self._bc().make(self, self._conv(other), ModFeature)

  def __truediv__(self: "FeatureGen", other: "FeatureGen") -> "FeatureGen":
    from declafe.binary import DivideFeature

    return self._bc().make(self, self._conv(other), DivideFeature)

  def __gt__(self: "FeatureGen", other):
    from declafe.binary import IsGreaterFeature

    return self._bc().make(self, self._conv(other), IsGreaterFeature)

  def __lt__(self: "FeatureGen", other):
    from declafe.binary import IsLessFeature

    return self._bc().make(self, self._conv(other), IsLessFeature)

  def __ge__(self: "FeatureGen", other):
    from declafe.binary import GEFeature

    return self._bc().make(self, self._conv(other), GEFeature)

  def __le__(self: "FeatureGen", other):
    from declafe.binary import LEFeature

    return self._bc().make(self, self._conv(other), LEFeature)