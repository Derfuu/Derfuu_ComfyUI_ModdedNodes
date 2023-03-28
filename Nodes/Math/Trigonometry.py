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
                "value": field.FLOAT,
                "type_": (["RAD", "DEG"],),
                "arcSin": ([False, True],)
            }
        }

    RETURN_TYPES = ("FLOAT",)
    FUNCTION = "get_value"
    CATEGORY = TREE_TRIGONOMETRY

    def get_value(self, value, type_="RAD", arcSin=False):
        if type_ == "DEG":
            value = math.radians(value)
        if arcSin == True:
            value = math.asin(value)
        else:
            value = math.sin(value)
        return (value,)


class CosNode:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):
        return {
            "required": {
                "value": field.FLOAT,
                "type_": (["RAD", "DEG"],),
                "arcCos": ([False, True],)
            }
        }

    RETURN_TYPES = ("FLOAT",)
    FUNCTION = "get_value"
    CATEGORY = TREE_TRIGONOMETRY

    def get_value(self, value, type_="RAD", arcCos=False):
        if type_ == "DEG":
            value = math.radians(value)
        if arcCos == True:
            value = math.acos(value)
        else:
            value = math.cos(value)
        return (value,)


class tgNode:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):
        return {
            "required": {
                "value": field.FLOAT,
                "type_": (["RAD", "DEG"],),
                "arcTan": ([False, True],)
            }
        }

    RETURN_TYPES = ("FLOAT",)
    FUNCTION = "get_value"
    CATEGORY = TREE_TRIGONOMETRY

    def get_value(self, value, type_="RAD", arcTan=False):
        if type_ == "DEG":
            value = math.radians(value)
        if arcTan == True:
            value = math.atan(value)
        else:
            value = math.tan(value)
        return (value,)