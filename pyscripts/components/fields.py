import sys

class AnyType(str):
    def __ne__(self, __value: object) -> bool:
        return False

FLOAT = ("FLOAT", {"default": 1,
                   "min": -sys.float_info.max,
                   "max": sys.float_info.max,
                   "step": 0.01})
# BOOL = ("BOOL", {"default": False})
INT = ("INT", {"default": 1,
               "min": -sys.maxsize,
               "max": sys.maxsize,
               "step": 1})
STRING = ("STRING", {"default": ""})
STRING_ML = ("STRING", {"multiline": True, "default": ""})
ANY = (AnyType("*"), {"forceInput": False})
