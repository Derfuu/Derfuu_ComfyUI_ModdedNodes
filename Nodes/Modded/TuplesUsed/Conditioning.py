import custom_nodes.Derfuu_ComfyUI_ModdedNodes.components.fields as field
from custom_nodes.Derfuu_ComfyUI_ModdedNodes.components.tree import TREE_TUPLE_CONDITIONING


class ConditioningSetArea:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):
        return {
            "required": {
                "conditioning": ("CONDITIONING",),
                "size_tuple": ("TUPLE",),
                "offset_tuple": ("TUPLE",),
                "strength": field.FLOAT,
            }
        }

    RETURN_TYPES = ("CONDITIONING",)
    FUNCTION = "append"
    CATEGORY = TREE_TUPLE_CONDITIONING

    def append(self, conditioning, size_tuple, offset_tuple, strength, min_sigma=0.0, max_sigma=99.0):

        width = int(size_tuple[0])
        height = int(size_tuple[1])

        x = int(offset_tuple[0])
        y = int(offset_tuple[1])

        c = []
        for t in conditioning:
            n = [t[0], t[1].copy()]
            # n[1]["area"].movedim(-1, 1)
            n[1]['area'] = (height // 8, width // 8, y // 8, x // 8)
            n[1]['strength'] = strength
            n[1]['min_sigma'] = min_sigma
            n[1]['max_sigma'] = max_sigma
            c.append(n)
        return (c,)