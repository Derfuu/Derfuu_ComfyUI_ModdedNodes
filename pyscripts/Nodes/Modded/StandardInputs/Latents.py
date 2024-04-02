from custom_nodes.Derfuu_ComfyUI_ModdedNodes.pyscripts.components.fields import Field

from custom_nodes.Derfuu_ComfyUI_ModdedNodes.pyscripts.components.tree import TREE_LATENTS
import custom_nodes.Derfuu_ComfyUI_ModdedNodes.pyscripts.components.sizes as sizes

import math
import comfy.utils


class LatentScale_Ratio:
    scale_methods = ["nearest-exact", "bilinear", "area"]
    crop_methods = ["disabled", "center"]

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "latent": Field.latent(),
                "modifier": Field.float(),
                "scale_method": Field.combo(cls.scale_methods),
                "crop": Field.combo(cls.crop_methods),
            }
        }

    RETURN_TYPES = ("LATENT",)
    FUNCTION = "scale"
    CATEGORY = TREE_LATENTS

    def scale(self, latent, scale_method, crop, modifier):

        size = sizes.get_latent_size(latent, True)

        lat_width = size[0]
        lat_height = size[1]
        #
        # width = latent["samples"][2]
        # height = latent["samples"][3]

        cls = latent.copy()
        cls["samples"] = comfy.utils.common_upscale(latent["samples"], lat_width // 8, lat_height // 8, scale_method, crop)
        return (cls,)


class LatentScale_Side:
    upscale_methods = ["nearest-exact", "bilinear", "area"]
    crop_methods = ["disabled", "center"]

    def __init__(self) -> None:
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "latent": Field.latent(),
                "side_length": Field.int(),
                "side": Field.combo(["Longest", "Shortest", "Width", "Height"]),
                "scale_method": Field.combo(cls.upscale_methods),
                "crop": Field.combo(cls.crop_methods)
            }
        }

    RETURN_TYPES = ("LATENT",)
    FUNCTION = "upscale"

    CATEGORY = TREE_LATENTS

    def upscale(self, latent, side_length: int, side: str, scale_method, crop):

        size = sizes.get_latent_size(latent, True)

        lat_width = size[0]
        lat_height = size[1]

        width = lat_width
        height = lat_height

        def determineSide(_side: str) -> tuple[int, int]:
            width, height = 0, 0
            if _side == "Width":
                heigh_ratio = lat_height / lat_width
                width = side_length
                height = heigh_ratio * width
            elif _side == "Height":
                width_ratio = lat_width / lat_height
                height = side_length
                width = width_ratio * height
            return width, height

        if side == "Longest":
            if width > height:
                width, height = determineSide("Width")
            else:
                width, height = determineSide("Height")
        elif side == "Shortest":
            if width < height:
                width, height = determineSide("Width")
            else:
                width, height = determineSide("Height")
        else:
            width, height = determineSide(side)


        width = math.ceil(width)
        height = math.ceil(height)

        cls = latent.copy()
        cls["samples"] = comfy.utils.common_upscale(latent["samples"], width // 8, height // 8, scale_method, crop)
        return (cls,)

  # 3rd option with both sides manually
