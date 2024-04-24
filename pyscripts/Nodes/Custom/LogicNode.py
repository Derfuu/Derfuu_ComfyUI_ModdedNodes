from ...components.fields import Field, ANY
from ...components.tree import TREE_FUNCTIONS

class LogicNode:
    def __init__(self) -> None:
        pass

    @classmethod
    def INPUT_TYPES(cls) -> dict:
        return {
            "required": {
                "Operation": Field.combo([
                    "A > B",
                    "A < B",
                    "A = B",
                    "A AND B",
                    "A OR B",
                    "A XOR B",
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

    def do_logic(self, CompareValue_A, CompareValue_B = False, OnTrue = False, OnFalse = False, Operation: str = "A AND B") -> tuple:
        match Operation:
            case "A > B":
                value = OnTrue if CompareValue_A > CompareValue_B else OnFalse
            case "A < B":
                value = OnTrue if CompareValue_A < CompareValue_B else OnFalse
            case "A = B":
                value = OnTrue if CompareValue_A == CompareValue_B else OnFalse
            case "A AND B":
                value = OnTrue if CompareValue_A and CompareValue_B else OnFalse
            case "A OR B":
                value = OnTrue if CompareValue_A or CompareValue_B else OnFalse
            case "A XOR B":
                value = OnTrue if not (CompareValue_A and CompareValue_B) and (CompareValue_A or CompareValue_B) else OnFalse
            case _:
                value = None
        return (value, )
