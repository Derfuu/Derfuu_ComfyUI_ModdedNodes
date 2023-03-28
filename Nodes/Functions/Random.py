import numpy.random

import custom_nodes.Derfuu_ComfyUI_ModdedNodes.components.fields as field

from custom_nodes.Derfuu_ComfyUI_ModdedNodes.components.tree import TREE_FUNCTIONS


class RandomValue:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Value_A": field.FLOAT,
                "Value_B": field.FLOAT,
            }
        }

    RETURN_TYPES = ("FLOAT",)
    FUNCTION = "get_rand"

    CATEGORY = TREE_FUNCTIONS

    def get_rand(self, Value_A, Value_B):
        value = numpy.random.uniform(Value_A, Value_B)
        return (value,)