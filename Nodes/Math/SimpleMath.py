import math

import custom_nodes.Derfuu_ComfyUI_ModdedNodes.components.fields as field
from custom_nodes.Derfuu_ComfyUI_ModdedNodes.components.tree import TREE_MATH


class MultiplyNode:
    def __init__(self) -> None:
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "FLOAT_A": field.FLOAT,
                "FLOAT_B": field.FLOAT,
            },
        }

    RETURN_TYPES = ("FLOAT",)
    FUNCTION = "multiply"
    CATEGORY = TREE_MATH

    def multiply(self, FLOAT_A, FLOAT_B):
        total = float(FLOAT_A * FLOAT_B)
        return (total,)


class DivideNode:
    def __init__(self) -> None:
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "FLOAT_A": field.FLOAT,
                "FLOAT_B": field.FLOAT,
            },
        }

    RETURN_TYPES = ("FLOAT",)
    FUNCTION = "divide"
    CATEGORY = TREE_MATH

    def divide(self, FLOAT_A, FLOAT_B):
        total = float(FLOAT_A / FLOAT_B)
        return (total,)


class SumNode:
    def __init__(self) -> None:
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "FLOAT_A": field.FLOAT,
                "FLOAT_B": field.FLOAT,
            },
        }

    RETURN_TYPES = ("FLOAT",)
    FUNCTION = "sum"
    CATEGORY = TREE_MATH

    def sum(self, FLOAT_A, FLOAT_B):
        total = float(FLOAT_A + FLOAT_B)
        return (total,)


class SubtractNode:
    def __init__(self) -> None:
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "FLOAT_A": field.FLOAT,
                "FLOAT_B": field.FLOAT,
            },
        }

    RETURN_TYPES = ("FLOAT",)
    FUNCTION = "sub"
    CATEGORY = TREE_MATH

    def sub(self, FLOAT_A, FLOAT_B):
        total = float(FLOAT_A - FLOAT_B)
        return (total,)


class PowNode:
    def __init__(self) -> None:
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "FLOAT_A": field.FLOAT,
                "FLOAT_B": field.FLOAT,
            },
        }

    RETURN_TYPES = ("FLOAT",)
    FUNCTION = "sub"
    CATEGORY = TREE_MATH

    def sub(self, FLOAT_A, FLOAT_B=2):
        total = math.pow(FLOAT_A, FLOAT_B)
        return (total,)


class SquareRootNode:
    def __init__(self) -> None:
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "FLOAT": field.FLOAT,
            },
        }

    RETURN_TYPES = ("FLOAT",)
    FUNCTION = "sub"
    CATEGORY = TREE_MATH

    def sub(self, FLOAT):
        total = math.sqrt(FLOAT)
        return (total,)