import custom_nodes.Derfuu_ComfyUI_CustomNodes.components.types as type
from custom_nodes.Derfuu_ComfyUI_CustomNodes.components.tree import TREE_DEBUG

class DebugNodeFloat:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "FLOAT": (type.FLOAT,),
            }
        }

    RETURN_TYPES = ()
    CATEGORY = TREE_DEBUG
    FUNCTION = "print_values"
    OUTPUT_NODE = True

    def print_values(self, FLOAT):
        print(FLOAT, sep="\n")
        return (None,)


class DebugNodeInt:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "INTEGER": (type.INT,),
            }
        }

    RETURN_TYPES = ()
    CATEGORY = TREE_DEBUG
    FUNCTION = "print_values"
    OUTPUT_NODE = True

    def print_values(self, INTEGER):
        print(INTEGER, sep="\n")
        return (None,)


class DebugNodeTuple:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "TUPLE": (type.TUPLE,),
            }
        }

    RETURN_TYPES = ()
    CATEGORY = TREE_DEBUG
    FUNCTION = "print_values"
    OUTPUT_NODE = True

    def print_values(self, TUPLE):
        print(TUPLE, sep="\n")
        return (None,)
