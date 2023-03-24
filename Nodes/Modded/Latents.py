import custom_nodes.Derfuu_ComfyUI_CustomNodes.components.types as type
import custom_nodes.Derfuu_ComfyUI_CustomNodes.components.fields as field

from custom_nodes.Derfuu_ComfyUI_CustomNodes.components.tree import TREE_LATENTS

import math
import torch
import comfy.utils


class EmptyLatentImage:
    def __init__(self, device="cpu"):
        self.device = device

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "TUPLE": (type.TUPLE,),
                "batch_size": field.INT,
            }
        }

    RETURN_TYPES = (type.LATENT,)
    FUNCTION = "generate"
    CATEGORY = TREE_LATENTS

    def generate(self, TUPLE, batch_size=1):
        width = int(TUPLE[0])
        height = int(TUPLE[1])

        latent = torch.zeros([batch_size, 4, height // 8, width // 8])
        return ({"samples": latent},)


class LatentScale_Ratio:
    scale_methods = (["nearest-exact", "bilinear", "area"],)
    crop_methods = (["disabled", "center"],)

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "LATENT": (type.LATENT,),
                "TUPLE": (type.TUPLE,),
                "modifier": field.FLOAT,
                "scale_method": cls.scale_methods,
                "crop": cls.crop_methods,
            }
        }

    RETURN_TYPES = (type.LATENT, type.TUPLE,)
    FUNCTION = "scale"
    CATEGORY = TREE_LATENTS

    def scale(self, LATENT, scale_method, crop, modifier, TUPLE=(None, None)):

        if TUPLE != (None, None):
            width = int(TUPLE[0] * modifier)
            height = int(TUPLE[1] * modifier)
        else:
            width = LATENT["samples"][2]
            height = LATENT["samples"][3]

        cls = LATENT.copy()
        cls["samples"] = comfy.utils.common_upscale(LATENT["samples"], width // 8, height // 8, scale_method, crop)
        return (cls, (width, height),)


class LatentScale_Side:
    upscale_methods = ["nearest-exact", "bilinear", "area"]
    crop_methods = ["disabled", "center"]

    def __init__(self) -> None:
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "LATENT": (type.LATENT,),
                "TUPLE": (type.TUPLE,),
                "side_length": field.INT,
                "side": (["Width", "Height"],),
                "scale_method": (cls.upscale_methods,),
                "crop": (cls.crop_methods,)}}

    RETURN_TYPES = (type.LATENT, type.TUPLE,)
    FUNCTION = "upscale"

    CATEGORY = TREE_LATENTS

    def upscale(self, LATENT, scale_method, TUPLE, side_length, side, crop):
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

        cls = LATENT.copy()
        cls["samples"] = comfy.utils.common_upscale(LATENT["samples"], width // 8, height // 8, scale_method, crop)
        return (cls, (width, height),)

  # 3rd option with both sides manually

class LatentComposite:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "SAMPLES_FROM": (type.LATENT,),
                "SAMPLES_TO": (type.LATENT,),
                "TUPLE_POSITION": (type.TUPLE,),
                "FEATHER": field.INT,
            }
        }

    RETURN_TYPES = (type.LATENT, type.FLOAT,)
    FUNCTION = "compose"
    CATEGORY = TREE_LATENTS

    def compose(self, SAMPLES_FROM, SAMPLES_TO, TUPLE_POSITION, FEATHER):
        x_off = int(TUPLE_POSITION[0] // 8)
        y_off = int(TUPLE_POSITION[1] // 8)
        feather = FEATHER // 8

        samples_out = SAMPLES_TO.copy()
        samples = SAMPLES_TO["samples"].clone()

        samples_to = SAMPLES_TO["samples"]
        samples_from = SAMPLES_FROM["samples"]

        if feather == 0:
            samples[:, :, y_off:y_off + samples_from.shape[2], x_off:x_off + samples_from.shape[3]] = \
               samples_from[:, :, :samples_to.shape[2] - y_off, :samples_to.shape[3] - x_off]
        else:
            samples_from = samples_from[:, :, :samples_to.shape[2] - y_off, :samples_to.shape[3] - x_off]
            mask = torch.ones_like(samples_from)
            for t in range(feather):
                if y_off != 0:
                    mask[:, :, t:1 + t, :] *= ((1.0 / feather) * (t + 1))

                if y_off + samples_from.shape[2] < samples_to.shape[2]:
                    mask[:, :, mask.shape[2] - 1 - t: mask.shape[2] - t, :] *= ((1.0 / feather) * (t + 1))
                if x_off != 0:
                    mask[:, :, :, t:1 + t] *= ((1.0 / feather) * (t + 1))
                if x_off + samples_from.shape[3] < samples_to.shape[3]:
                    mask[:, :, :, mask.shape[3] - 1 - t: mask.shape[3] - t] *= ((1.0 / feather) * (t + 1))
            rev_mask = torch.ones_like(mask) - mask
            samples[:, :, y_off:y_off + samples_from.shape[2], x_off:x_off + samples_from.shape[3]] = \
                samples_from[:, :, :samples_to.shape[2] - y_off, :samples_to.shape[3] - x_off] * \
                mask + samples[:, :, y_off:y_off + samples_from.shape[2], x_off:x_off + samples_from.shape[3]] *\
                rev_mask
        samples_out["samples"] = samples
        return (samples_out, FEATHER,)