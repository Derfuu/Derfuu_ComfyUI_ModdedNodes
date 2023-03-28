def get_latent_size(LATENT, ORIGINAL_VALUES=False):
    lc = LATENT.copy()
    size = lc["samples"].shape[3], lc["samples"].shape[2]
    if ORIGINAL_VALUES == False:
        size = size[0] * 8, size[1] * 8
    return size

def get_image_size(IMAGE):
    samples = IMAGE.movedim(-1, 1)
    size = samples.shape[3], samples.shape[2]
    # size = size.movedim(1, -1)
    return size

def get_conditioning_size(CONDITIONING):
    size = CONDITIONING["area"]
    width = size[1]
    height = size[0]
    x_offs = size[3]
    y_offs = size[2]
    return ({"w": width, "h": height},{"x": x_offs, "y":y_offs})