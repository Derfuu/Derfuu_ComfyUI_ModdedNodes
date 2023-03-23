import math
import custom_nodes.Derfuu_ComfyUI_CustomNodes.components.types as type
import custom_nodes.Derfuu_ComfyUI_CustomNodes.components.fields as field
from custom_nodes.Derfuu_ComfyUI_CustomNodes.components.tree import TREE_VARIABLE, TREE_TUPLES

class FloatNode:
    def __init__(self) -> None:
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "VALUE": field.FLOAT,
            },
        }

    RETURN_TYPES = (type.FLOAT,)
    CATEGORY = TREE_VARIABLE
    FUNCTION = "get_value"

    def get_value(self, VALUE):
        return (VALUE,)


class IntegerNode:
    def __init__(self) -> None:
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "VALUE": field.INT,
            },
        }

    RETURN_TYPES = (type.INT,)
    CATEGORY = TREE_VARIABLE
    FUNCTION = "get_value"

    def get_value(self, VALUE):
        return (VALUE,)


class TupleNode:
    def __init__(self):
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

    RETURN_TYPES = (type.TUPLE,)
    CATEGORY = TREE_VARIABLE

    FUNCTION = 'get_value'

    def get_value(self, FLOAT_A, FLOAT_B, Ceil2Int="false"):
        if Ceil2Int == "true":
            FLOAT_A = math.ceil(FLOAT_A)
            FLOAT_B = math.ceil(FLOAT_B)
        return ((FLOAT_A, FLOAT_B),)


class StringNode:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "VALUE": field.STRING,
            }
        }

    RETURN_TYPES = (type.STRING,)
    FUNCTION = "get_value"
    CATEGORY = TREE_VARIABLE

    def get_value(self, VALUE):
        return (VALUE,)


class MultilineStringNode:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "VALUE": field.STRING_ML,
            }
        }

    RETURN_TYPES = (type.STRING,)
    FUNCTION = "get_value"
    CATEGORY = TREE_VARIABLE

    def get_value(self, VALUE):
        return (VALUE,)


