import custom_nodes.Derfuu_ComfyUI_ModdedNodes.components.fields as field

from custom_nodes.Derfuu_ComfyUI_ModdedNodes.components.tree import TREE_FUNCTIONS
import custom_nodes.Derfuu_ComfyUI_ModdedNodes.components.sizes as sizes_DF


class GetLatentSize:
    def __init__(self) -> None:
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "LATENT": ("LATENT",),
                "ORIGINAL_VALUES": ([False, True],),
            }
        }

    RETURN_TYPES = ("TUPLE", "INT", "INT",)
    CATEGORY = TREE_FUNCTIONS

    FUNCTION = 'get_size'

    def get_size(self, LATENT, ORIGINAL_VALUES=False):
        size = sizes_DF.get_latent_size(LATENT, ORIGINAL_VALUES)
        return (size, size[0], size[1],)


class GetImageSize:
    def __init__(self) -> None:
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "IMAGE": ("IMAGE",),
            }
        }

    RETURN_TYPES = ("TUPLE", "INT", "INT",)
    CATEGORY = TREE_FUNCTIONS

    FUNCTION = 'get_size'

    def get_size(self, IMAGE):
        size = sizes_DF.get_image_size(IMAGE)
        return (size, size[0], size[1],)