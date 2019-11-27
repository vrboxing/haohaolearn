#! /usr/bin/python3
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd

obj = pd.Series([4, 7, -5, 3])
obj.values
obj.index
obj2 = pd.Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
obj2
obj2['a']
obj2['d'] = 6
obj2[obj2 > 0]
obj2 * 2
obj2
np.exp(obj2)