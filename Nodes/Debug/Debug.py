import sys

import custom_nodes.Derfuu_ComfyUI_ModdedNodes.components.fields as field
from custom_nodes.Derfuu_ComfyUI_ModdedNodes.components.tree import TREE_DEBUG

class DebugNodeFloat:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Prefix": field.STRING,
                "Value": field.FLOAT,
            }
        }

    RETURN_TYPES = ()
    CATEGORY = TREE_DEBUG
    FUNCTION = "print_values"
    OUTPUT_NODE = True

    def print_values(self, Value, Prefix):
        print(f"{Prefix}: {Value}", sep="\n")
        return (None,)


class DebugNodeInt:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Prefix": field.STRING,
                "Value": field.INT,
            }
        }

    RETURN_TYPES = ()
    CATEGORY = TREE_DEBUG
    FUNCTION = "print_values"
    OUTPUT_NODE = True

    def print_values(self, Value, Prefix):
        print(f"{Prefix}: {Value}", sep="\n")
        return (None,)


class DebugNodeTuple:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Prefix": field.STRING,
                "Values": ("TUPLE",),
            }
        }

    RETURN_TYPES = ()
    CATEGORY = TREE_DEBUG
    FUNCTION = "print_values"
    OUTPUT_NODE = True

    def print_values(self, Values, Prefix):
        print(f"{Prefix}: {Values}", sep="\n")
        return (None,)

class DebugNodeString:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Prefix": field.STRING,
                "Text": field.STRING,
            }
        }

    RETURN_TYPES = ()
    CATEGORY = TREE_DEBUG
    FUNCTION = "print_values"
    OUTPUT_NODE = True

    def print_values(self, Text, Prefix):
        print(f"{Prefix}: {Text}", sep="\n")
        return (None,)