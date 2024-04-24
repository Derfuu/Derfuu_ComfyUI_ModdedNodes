import sys
from numpy import random

from ...components.fields import Field
from ...components.tree import TREE_FUNCTIONS


class RandomValue:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Value_A": Field.float(default=0),
                "Value_B": Field.float(default=1),
                "seed": Field.int(default=0, min=0, max=2**32-1),
            }
        }

    RETURN_TYPES = ("FLOAT",)
    FUNCTION = "get_rand"

    CATEGORY = TREE_FUNCTIONS

    def get_rand(self, Value_A, Value_B, seed):
        random.seed(seed)
        value = random.uniform(Value_A, Value_B)
        return (value,)
