import custom_nodes.Derfuu_ComfyUI_ModdedNodes.components.fields as field

import math

from custom_nodes.Derfuu_ComfyUI_ModdedNodes.components.tree import TREE_TUPLES


class Tuple:
    def __init__(self) -> None:
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Value_A": field.FLOAT,
                "Value_B": field.FLOAT,
                "round_": (["No", "Yes", "Ceil", "Floor"],),
            }
        }

    RETURN_TYPES = ("TUPLE",)
    CATEGORY = TREE_TUPLES

    FUNCTION = 'get_tuple'

    def get_tuple(self, Value_A: float = 0, Value_B: float = 0, round_: str = "No"):
        if round_ == "No":
            return ((Value_A, Value_B),)
        elif round_ == "Yes":
            return ((round(Value_A), round(Value_B)),)
        elif round_ == "Ceil":
            return ((math.ceil(Value_A), math.ceil(Value_B)),)
        elif round_ == "Floor":
            return ((math.floor(Value_A), math.floor(Value_B)),)
        # py 3.10+
        # match round:
        #     case "No":
        #         return ((Value_A, Value_B),)
        #     case "Yes":
        #         return ((int(Value_A), int(Value_B)),)
        #     case "Ceil":
        #         return ((math.ceil(Value_A), math.ceil(Value_B)),)
        #     case "Floor":
        #         return ((math.floor(Value_A), math.floor(Value_B)),)


class Int2Tuple:
    def __init__(self) -> None:
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Value_A": field.INT,
                "Value_B": field.INT,
            }
        }

    RETURN_TYPES = ("TUPLE",)
    CATEGORY = TREE_TUPLES

    FUNCTION = 'get_tuple'

    def get_tuple(self, Value_A=0, Value_B=0):
        return ((Value_A, Value_B),)


class Tuple2Float:
    def __init__(self) -> None:
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Tuple": ("TUPLE",),
            }
        }

    RETURN_TYPES = ("FLOAT", "FLOAT",)
    CATEGORY = TREE_TUPLES

    FUNCTION = 'get_tuple'

    def get_tuple(self, Tuple):
        return (Tuple[0], Tuple[1],)

class Tuple2Int:
    def __init__(self) -> None:
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Tuple": ("TUPLE",),
            }
        }

    RETURN_TYPES = ("INT", "INT",)
    CATEGORY = TREE_TUPLES

    FUNCTION = 'get_tuple'

    def get_tuple(self, Tuple):
        return (int(Tuple[0]), int(Tuple[1]),)


class FlipTuple:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Tuple": ("TUPLE",)
            }
        }

    RETURN_TYPES = ("TUPLE",)
    FUNCTION = "flip"
    CATEGORY = TREE_TUPLES

    def flip(self, Tuple):
        return ((Tuple[1], Tuple[0]),)



class MultiplyTupleBy:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required":{
                "Tuple": ("TUPLE",),
                "Value": field.FLOAT,
            }
        }

    RETURN_TYPES = ("TUPLE",)
    FUNCTION = "MultiplyTuples"
    CATEGORY = TREE_TUPLES

    def MultiplyTuples(self, Tuple: tuple, Value: float):
        Tuple = (
            Tuple[0] * Value,
            Tuple[1] * Value
        )
        return (Tuple,)
