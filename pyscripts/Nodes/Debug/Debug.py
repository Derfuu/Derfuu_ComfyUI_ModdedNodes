from ...components.fields import Field, ANY
from ...components.colors import colorize, ConsoleColor
from ...components.tree import TREE_DEBUG

class ShowDataDebug:
    CATEGORY = TREE_DEBUG

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "ANY": Field.any(),
            },
        }

    RETURN_TYPES = (ANY, "STRING", )
    RETURN_NAMES = ("SAME AS INPUT", "STRING", )
    OUTPUT_NODE = True
    IS_CHANGED = True
    FUNCTION = "func"

    def func(self, ANY = None):
        out = ANY
        try:
            out = str(out)
            print(colorize(f"[DEBUG]: {ANY}", ConsoleColor.blue.value))
        except Exception as e:
            print(colorize(f"[DEBUG-EXCEPTION]: {e}", ConsoleColor.bold_red.value))
            out = str(e)
        return {"ui": {"text": [out]}, "result": (ANY, out)}
