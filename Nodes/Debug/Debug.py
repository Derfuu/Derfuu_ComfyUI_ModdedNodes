import custom_nodes.Derfuu_ComfyUI_ModdedNodes.components.types as type
import custom_nodes.Derfuu_ComfyUI_ModdedNodes.components.fields as field
from custom_nodes.Derfuu_ComfyUI_ModdedNodes.components.tree import TREE_DEBUG

class DebugNodeFloat:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "TITLE": field.STRING,
                "FLOAT": (type.FLOAT,),
            }
        }

    RETURN_TYPES = ()
    CATEGORY = TREE_DEBUG
    FUNCTION = "print_values"
    OUTPUT_NODE = True

    def print_values(self, FLOAT, TITLE):
        print(f"{TITLE}: {FLOAT}", sep="\n")
        return (None,)


class DebugNodeInt:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "TITLE": field.STRING,
                "INTEGER": (type.INT,),
            }
        }

    RETURN_TYPES = ()
    CATEGORY = TREE_DEBUG
    FUNCTION = "print_values"
    OUTPUT_NODE = True

    def print_values(self, INTEGER, TITLE):
        print(f"{TITLE}: {INTEGER}", sep="\n")
        return (None,)


class DebugNodeTuple:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "TITLE": field.STRING,
                "TUPLE": (type.TUPLE,),
            }
        }

    RETURN_TYPES = ()
    CATEGORY = TREE_DEBUG
    FUNCTION = "print_values"
    OUTPUT_NODE = True

    def print_values(self, TUPLE, TITLE):
        print(f"{TITLE}: {TUPLE}", sep="\n")
        return (None,)
