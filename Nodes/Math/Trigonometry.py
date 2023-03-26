import custom_nodes.Derfuu_ComfyUI_ModdedNodes.components.fields as field
from custom_nodes.Derfuu_ComfyUI_ModdedNodes.components.tree import TREE_TRIGONOMETRY

import math

class SinNode:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):
        return {
            "required": {
                "FLOAT": field.FLOAT,
                "INPUT_TYPE": (["RAD", "DEG"],),
                "arcSin": ([False, True],)
            }
        }

    RETURN_TYPES = ("FLOAT",)
    FUNCTION = "get_value"
    CATEGORY = TREE_TRIGONOMETRY

    def get_value(self, FLOAT, INPUT_TYPE="RAD", arcSin=False):
        if INPUT_TYPE == "DEG":
            FLOAT = math.radians(FLOAT)
        if arcSin == True:
            FLOAT = math.asin(FLOAT)
        else:
            FLOAT = math.sin(FLOAT)
        return (FLOAT,)


class CosNode:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):
        return {
            "required": {
                "FLOAT": field.FLOAT,
                "INPUT_TYPE": (["RAD", "DEG"],),
                "arcCos": ([False, True],)
            }
        }

    RETURN_TYPES = ("FLOAT",)
    FUNCTION = "get_value"
    CATEGORY = TREE_TRIGONOMETRY

    def get_value(self, FLOAT, INPUT_TYPE="RAD", arcCos=False):
        if INPUT_TYPE == "DEG":
            FLOAT = math.radians(FLOAT)
        if arcCos == True:
            FLOAT = math.acos(FLOAT)
        else:
            FLOAT = math.cos(FLOAT)
        return (FLOAT,)


class tgNode:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):
        return {
            "required": {
                "FLOAT": field.FLOAT,
                "INPUT_TYPE": (["RAD", "DEG"],),
                "arcTan": ([False, True],)
            }
        }

    RETURN_TYPES = ("FLOAT",)
    FUNCTION = "get_value"
    CATEGORY = TREE_TRIGONOMETRY

    def get_value(self, FLOAT, INPUT_TYPE="RAD", arcTan=False):
        if INPUT_TYPE == "DEG":
            FLOAT = math.radians(FLOAT)
        if arcTan == True:
            FLOAT = math.atan(FLOAT)
        else:
            FLOAT = math.tan(FLOAT)
        return (FLOAT,)