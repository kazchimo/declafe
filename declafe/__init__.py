from typing import Union

import numpy

from declafe.feature_gen.FeatureGen import *
from .Features import *
from .ComposedFeature import *
from .ConstFeature import *

series = Union[pd.Series, numpy.ndarray]
