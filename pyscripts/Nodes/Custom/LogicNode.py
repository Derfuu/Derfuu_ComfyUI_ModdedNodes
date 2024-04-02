from custom_nodes.Derfuu_ComfyUI_ModdedNodes.pyscripts.components.fields import Field, ANY
from custom_nodes.Derfuu_ComfyUI_ModdedNodes.pyscripts.components.tree import TREE_FUNCTIONS

class LogicNode:
    def __init__(self) -> None:
        pass

    @classmethod
    def INPUT_TYPES(cls) -> dict:
        return {
            "required": {
                "Operation": Field.combo([
                    ">", "<", "=", "AND", "OR", "XOR",
                ]),
                "CompareValue_A": Field.any(),
            },
            "optional": {
                "CompareValue_B": Field.any(),
                "OnTrue": Field.any(),
                "OnFalse": Field.any()
            }
        }

    RETURN_TYPES = (ANY,)
    CATEGORY = TREE_FUNCTIONS
    FUNCTION = "do_logic"

    def do_logic(self, CompareValue_A, CompareValue_B = False, OnTrue = False, OnFalse = False, Operation: str = "AND") -> tuple:
        match Operation:
            case ">":
                value = OnTrue if CompareValue_A > CompareValue_B else OnFalse
            case "<":
                value = OnTrue if CompareValue_A < CompareValue_B else OnFalse
            case "=":
                value = OnTrue if CompareValue_A == CompareValue_B else OnFalse
            case "AND":
                value = OnTrue if CompareValue_A and CompareValue_B else OnFalse
            case "OR":
                value = OnTrue if CompareValue_A or CompareValue_B else OnFalse
            case "XOR":
                value = OnTrue if not (CompareValue_A and CompareValue_B) and (CompareValue_A or CompareValue_B) else OnFalse
            case _:
                value = None
        return (value, )
