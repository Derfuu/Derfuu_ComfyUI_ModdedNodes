import logging

from custom_nodes.Derfuu_ComfyUI_ModdedNodes.pyscripts.components.fields import Field, ANY
from custom_nodes.Derfuu_ComfyUI_ModdedNodes.pyscripts.components.tree import TREE_DEBUG

from custom_nodes.Derfuu_ComfyUI_ModdedNodes.pyscripts.components.colours import colorize, ConsoleColor

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
            print(colorize(f"[DEBUG]: {ANY}", ConsoleColor.blue.value))
        except Exception as e:
            print(colorize(f"[DEBUG-EXCEPTION]: {e}", ConsoleColor.bold_red.value))
            out = str(e)
        return {"ui": {"text": [out]}, "result": (ANY, [out])}
