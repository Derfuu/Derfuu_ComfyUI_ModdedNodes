import custom_nodes.Derfuu_ComfyUI_CustomNodes.components.types as type

import math

from custom_nodes.Derfuu_ComfyUI_CustomNodes.components.tree import TREE_FUNCTIONS


class Float2Tuple:
    def __init__(self) -> None:
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "FLOAT_A": (type.FLOAT,),
                "FLOAT_B": (type.FLOAT,),
                "Ceil2Int": ([False, True],),
            }
        }

    RETURN_TYPES = (type.TUPLE,)
    CATEGORY = TREE_FUNCTIONS

    FUNCTION = 'get_tuple'

    def get_tuple(self, FLOAT_A=0, FLOAT_B=0, Ceil2Int="false"):
        if Ceil2Int == "true":
            FLOAT_A = math.ceil(FLOAT_A)
            FLOAT_B = math.ceil(FLOAT_B)
        return ((FLOAT_A, FLOAT_B),)


class Tuple2Float:
    def __init__(self) -> None:
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "TUPLE": (type.TUPLE,),
            }
        }

    RETURN_TYPES = (type.FLOAT, type.FLOAT,)
    CATEGORY = TREE_FUNCTIONS

    FUNCTION = 'get_tuple'

    def get_tuple(self, TUPLE):
        return (TUPLE[0], TUPLE[1],)


class FlipTuple:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "TUPLE": (type.TUPLE,)
            }
        }

    RETURN_TYPES = (type.TUPLE,)
    FUNCTION = "flip"
    CATEGORY = TREE_FUNCTIONS

    def flip(self, TUPLE):
        return ((TUPLE[1], TUPLE[0]),)


class MergeTuples:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "TUPLE_A": (type.TUPLE,),
                "TUPLE_B": (type.TUPLE,),
            }
        }

    RETURN_TYPES = (type.TUPLE,)
    FUNCTION = "merge"
    CATEGORY = TREE_FUNCTIONS

    def merge(self, TUPLE_A, TUPLE_B):
        return ((TUPLE_A, TUPLE_B),)


class Tuple2Tuple:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "TUPLE": (type.TUPLE,),
            }
        }

    RETURN_TYPES = (type.TUPLE, type.TUPLE,)
    FUNCTION = "spl"
    CATEGORY = TREE_FUNCTIONS

    def spl(self, TUPLE):
        return (TUPLE[0], TUPLE[1],)
