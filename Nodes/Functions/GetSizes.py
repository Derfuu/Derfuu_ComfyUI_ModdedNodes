import custom_nodes.Derfuu_ComfyUI_CustomNodes.components.types as type

from custom_nodes.Derfuu_ComfyUI_CustomNodes.components.tree import TREE_FUNCTIONS


class GetLatentSize:
    def __init__(self) -> None:
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "LATENT": (type.LATENT,),
                "ORIGINAL_VALUES": ([False, True],),
            }
        }

    RETURN_TYPES = (type.TUPLE,)
    CATEGORY = TREE_FUNCTIONS

    FUNCTION = 'get_size'

    def get_size(self, LATENT, ORIGINAL_VALUES=False):
        lc = LATENT.copy()
        size = lc["samples"].shape[3], lc["samples"].shape[2]
        if ORIGINAL_VALUES == False:
            size = size[0] * 8, size[1] * 8
        return (size,)


class GetImageSize:
    def __init__(self) -> None:
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "IMAGE": (type.IMAGE,),
            }
        }

    RETURN_TYPES = (type.TUPLE,)
    CATEGORY = TREE_FUNCTIONS

    FUNCTION = 'get_size'

    def get_size(self, IMAGE):
        samples = IMAGE.movedim(-1, 1)
        size = samples.shape[3], samples.shape[2]
        # size = size.movedim(1, -1)
        return (size,)