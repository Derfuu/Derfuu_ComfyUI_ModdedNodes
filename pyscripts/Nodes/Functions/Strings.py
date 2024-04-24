import re
from ...components.tree import TREE_STRINGS
from ...components.fields import Field


class StringConcat:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Prepend": Field.string(),
                "Append": Field.string(),
                "Delimiter": Field.string(default=", ")
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("TEXT",)
    FUNCTION = "concatenate"
    CATEGORY = TREE_STRINGS

    def concatenate(self, Prepend, Append, Delimiter):
        out = f"{Prepend}{Delimiter}{Append}"
        return (out,)


class StringReplace:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Text": Field.string(),
                "Pattern": Field.string(),
                "Replace_With": Field.string(),
                "Mode": Field.combo(["Strict", "RegEx"]),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("TEXT",)
    FUNCTION = "replace"
    CATEGORY = TREE_STRINGS

    def replace(self, Text, Pattern, Replace_With, Mode):
        out = Text
        match Mode:
            case "Strict":
                out = Text.replace(Pattern, Replace_With)
            case "RegEx":
                out = re.sub(Pattern, Replace_With, Text)
        return (out,)
