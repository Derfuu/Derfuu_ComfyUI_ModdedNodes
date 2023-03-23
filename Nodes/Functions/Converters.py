import custom_nodes.Derfuu_ComfyUI_CustomNodes.components.types as type

import math

from custom_nodes.Derfuu_ComfyUI_CustomNodes.components.tree import TREE_CONVERTERS


class Int2Float:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "INT": (type.INT,),
            }
        }

    RETURN_TYPES = (type.FLOAT,)
    FUNCTION = "get_value"
    CATEGORY = TREE_CONVERTERS

    def get_value(self, INT):
        return (float(INT),)


class CeilNode:
    def __init__(self) -> None:
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "FLOAT": (type.FLOAT,),
            }
        }

    RETURN_TYPES = (type.INT,)
    FUNCTION = "get_value"
    CATEGORY = TREE_CONVERTERS

    def get_value(self, FLOAT):
        total = int(math.ceil(FLOAT))
        return (total,)


class FloorNode:
    def __init__(self) -> None:
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "FLOAT": (type.FLOAT,),
            }
        }

    RETURN_TYPES = (type.INT,)
    FUNCTION = "get_value"
    CATEGORY = TREE_CONVERTERS

    def get_value(self, FLOAT):
        total = int(math.floor(FLOAT))
        return (total,)


class ABSNode:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):
        return {
            "required": {
                "FLOAT": (type.FLOAT,),
                "IsNegative": ([False, True],)
            }
        }

    RETURN_TYPES = (type.FLOAT,)
    FUNCTION = "abs_val"
    CATEGORY = TREE_CONVERTERS

    def abs_val(self, FLOAT, IsNegative):
        if IsNegative:
            return (-abs(FLOAT),)
        return (abs(FLOAT),)