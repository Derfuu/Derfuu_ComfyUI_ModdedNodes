import custom_nodes.Derfuu_ComfyUI_ModdedNodes.components.fields as field

from custom_nodes.Derfuu_ComfyUI_ModdedNodes.components.tree import TREE_COND


class ConditioningSetArea_MOD:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):
        return {
            "required": {
                "CONDITIONING": ("CONDITIONING",),
                "SIZE_TUPLE": ("TUPLE",),
                "OFFSET_TUPLE": ("TUPLE",),
                "STRENGTH": field.FLOAT,
            }
        }

    RETURN_TYPES = ("CONDITIONING",)
    FUNCTION = "append"
    CATEGORY = TREE_COND

    def append(self, CONDITIONING, SIZE_TUPLE, OFFSET_TUPLE, STRENGTH, min_sigma=0.0, max_sigma=99.0):

        width = int(SIZE_TUPLE[0])
        height = int(SIZE_TUPLE[1])

        x = int(OFFSET_TUPLE[0])
        y = int(OFFSET_TUPLE[1])

        c = []
        for t in CONDITIONING:
            n = [t[0], t[1].copy()]
            # n[1]["area"].movedim(-1, 1)
            n[1]['area'] = (height // 8, width // 8, y // 8, x // 8)
            n[1]['strength'] = STRENGTH
            n[1]['min_sigma'] = min_sigma
            n[1]['max_sigma'] = max_sigma
            c.append(n)
        return (c,)