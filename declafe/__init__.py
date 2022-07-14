from typing import Union

import numpy

from .feature_gen import *
from .Features import *
from .ComposedFeature import *
from .ConstFeature import *

series = Union[pd.Series, numpy.ndarray]
