from typing import Union

import numpy
import pandas as pd

from .ComposedFeature import *
from .ConstFeature import *
from .Features import *
from .feature_gen.FeatureGen import *

series = Union[pd.Series, numpy.ndarray]
