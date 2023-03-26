import custom_nodes.Derfuu_ComfyUI_ModdedNodes.components.fields as field

from custom_nodes.Derfuu_ComfyUI_ModdedNodes.components.tree import TREE_IMAGES

import math
import comfy.utils


class ImageScale_Ratio:
    upscale_methods = ["nearest-exact", "bilinear", "area"]
    crop_methods = ["disabled", "center"]

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "IMAGE": ("IMAGE",),
                "TUPLE": ("TUPLE",),
                "modifier": field.FLOAT,
                "upscale_method": (cls.upscale_methods,),
                "crop": (cls.crop_methods,)}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "upscale"

    CATEGORY = TREE_IMAGES

    def upscale(self, IMAGE, upscale_method, TUPLE, modifier, crop):
        samples = IMAGE.movedim(-1, 1)

        width_B = int(TUPLE[0])
        height_B = int(TUPLE[1])

        height = math.ceil(height_B * modifier)
        width = math.ceil(width_B * modifier)
        cls = comfy.utils.common_upscale(samples, width, height, upscale_method, crop)
        cls = cls.movedim(1, -1)
        return (cls,)


class ImageScale_Side:
    upscale_methods = ["nearest-exact", "bilinear", "area"]
    crop_methods = ["disabled", "center"]

    def __init__(self) -> None:
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "IMAGE": ("IMAGE",),
                "TUPLE": ("TUPLE",),
                "side_length": field.INT,
                "side": (["Width", "Height"],),
                "upscale_method": (cls.upscale_methods,),
                "crop": (cls.crop_methods,)}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "upscale"

    CATEGORY = TREE_IMAGES

    def upscale(self, IMAGE, upscale_method, TUPLE, side_length, side, crop):
        samples = IMAGE.movedim(-1, 1)

        width_B = int(TUPLE[0])
        height_B = int(TUPLE[1])

        width = width_B
        height = height_B

        if side == "Width":
            heigh_ratio = height_B / width_B
            width = side_length
            height = heigh_ratio * width
        elif side == "Height":
            width_ratio = width_B / height_B
            height = side_length
            width = width_ratio * height

        width = math.ceil(width)
        height = math.ceil(height)

        cls = comfy.utils.common_upscale(samples, width, height, upscale_method, crop)
        cls = cls.movedim(1, -1)
        return (cls,)