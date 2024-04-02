from custom_nodes.Derfuu_ComfyUI_ModdedNodes.pyscripts.components.fields import Field, ANY
from custom_nodes.Derfuu_ComfyUI_ModdedNodes.pyscripts.components.tree import TREE_DEBUG

class ShowDataDebug:
    CATEGORY = TREE_DEBUG

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "ANY": Field.any(),
            },
        }

    OUTPUT_IS_LIST = (False, True, )
    RETURN_TYPES = (ANY, "STRING", )
    RETURN_NAMES = ("SAME AS INPUT", "STRING", )
    OUTPUT_NODE = True
    FUNCTION = "func"

    def func(self, ANY = None):
        out = ANY
        try:
            out = str(out)
            print(f"[DEBUG]: {ANY}")
        except Exception as e:
            print(f"[DEBUG-EXCEPTION]: {e}")
            out = str(e)
        return {"ui": {"text": [out]}, "result": (ANY, [out])}
