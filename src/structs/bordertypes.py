# -*- coding: utf-8 -*-
from enum import Enum

class BorderTypes(Enum):
    """Class to enumerate border types
    """
    normal = 0
    double = 2
    simple = 3
    simplest = 4
    rounded = 5
    quadrant = 6
    shade_light = 7
    shade_medium = 8
    shade_dark = 9
    density = 10
