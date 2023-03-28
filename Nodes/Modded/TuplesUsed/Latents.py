import custom_nodes.Derfuu_ComfyUI_ModdedNodes.components.fields as field

from custom_nodes.Derfuu_ComfyUI_ModdedNodes.components.tree import TREE_TUPLE_LATENTS
import custom_nodes.Derfuu_ComfyUI_ModdedNodes.components.sizes as sizes

import torch

class LatentComposite:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "samples_to": ("LATENT",),
                "samples_from": ("LATENT",),
                "position_tuple": ("TUPLE",),
                "feather": field.INT,
            }
        }

    RETURN_TYPES = ("LATENT",)
    FUNCTION = "compose"
    CATEGORY = TREE_TUPLE_LATENTS

    def compose(self, samples_from, samples_to, position_tuple, feather):
        x_off = int(position_tuple[0] // 8)
        y_off = int(position_tuple[1] // 8)
        feather = feather // 8

        samples_out = samples_to.copy()
        samples = samples_to["samples"].clone()

        samples_to = samples_to["samples"]
        samples_from = samples_from["samples"]

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
        return (samples_out,)