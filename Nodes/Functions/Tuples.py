import custom_nodes.Derfuu_ComfyUI_ModdedNodes.components.fields as field

import math

from custom_nodes.Derfuu_ComfyUI_ModdedNodes.components.tree import TREE_TUPLES


class Float2Tuple:
    def __init__(self) -> None:
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "FLOAT_A": field.FLOAT,
                "FLOAT_B": field.FLOAT,
                "Ceil2Int": ([False, True],),
            }
        }

    RETURN_TYPES = ("TUPLE",)
    CATEGORY = TREE_TUPLES

    FUNCTION = 'get_tuple'

    def get_tuple(self, FLOAT_A=0, FLOAT_B=0, Ceil2Int=False):
        if Ceil2Int == True:
            FLOAT_A = math.ceil(FLOAT_A)
            FLOAT_B = math.ceil(FLOAT_B)
        return ((FLOAT_A, FLOAT_B),)


class Int2Tuple:
    def __init__(self) -> None:
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "INT_A": field.INT,
                "INT_B": field.INT,
            }
        }

    RETURN_TYPES = ("TUPLE",)
    CATEGORY = TREE_TUPLES

    FUNCTION = 'get_tuple'

    def get_tuple(self, INT_A=0, INT_B=0):
        return ((INT_A, INT_B),)


class Tuple2Float:
    def __init__(self) -> None:
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "TUPLE": ("TUPLE",),
            }
        }

    RETURN_TYPES = ("FLOAT", "FLOAT",)
    CATEGORY = TREE_TUPLES

    FUNCTION = 'get_tuple'

    def get_tuple(self, TUPLE):
        return (TUPLE[0], TUPLE[1],)

class Tuple2Int:
    def __init__(self) -> None:
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "TUPLE": ("TUPLE",),
            }
        }

    RETURN_TYPES = ("INT", "INT",)
    CATEGORY = TREE_TUPLES

    FUNCTION = 'get_tuple'

    def get_tuple(self, TUPLE):
        return (int(TUPLE[0]), int(TUPLE[1]),)


class FlipTuple:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "TUPLE": ("TUPLE",)
            }
        }

    RETURN_TYPES = ("TUPLE",)
    FUNCTION = "flip"
    CATEGORY = TREE_TUPLES

    def flip(self, TUPLE):
        return ((TUPLE[1], TUPLE[0]),)


class MergeTuples:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "TUPLE_A": ("TUPLE",),
                "TUPLE_B": ("TUPLE",),
            }
        }

    RETURN_TYPES = ("TUPLE",)
    FUNCTION = "merge"
    CATEGORY = TREE_TUPLES

    def merge(self, TUPLE_A, TUPLE_B):
        return ((TUPLE_A, TUPLE_B),)


class Tuple2Tuple:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "TUPLE": ("TUPLE",),
            }
        }

    RETURN_TYPES = ("TUPLE", "TUPLE",)
    FUNCTION = "spl"
    CATEGORY = TREE_TUPLES

    def spl(self, TUPLE):
        return (TUPLE[0], TUPLE[1],)
