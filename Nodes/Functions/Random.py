import numpy.random

import custom_nodes.Derfuu_ComfyUI_ModdedNodes.components.types as type
import custom_nodes.Derfuu_ComfyUI_ModdedNodes.components.fields as field

from custom_nodes.Derfuu_ComfyUI_ModdedNodes.components.tree import TREE_FUNCTIONS


class RandomValue:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "VALUE_UP": field.FLOAT,
                "VALUE_BOT": field.FLOAT,
            }
        }

    RETURN_TYPES = (type.FLOAT,)
    FUNCTION = "get_rand"
    CATEGORY = TREE_FUNCTIONS

    def get_rand(self, VALUE_UP, VALUE_BOT):
        value = numpy.random.uniform(VALUE_UP, VALUE_BOT)
        return (value,)