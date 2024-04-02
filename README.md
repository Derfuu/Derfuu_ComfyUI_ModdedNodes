# Derfuu_ComfyUI_ModdedNodes

- **ComfyUI**: [LINK](https://github.com/comfyanonymous/ComfyUI)

## Small description
- Automate calculation depending on image sizes or something you want
- Easier(or not) editing multiple values of various nodes
- Math nodes
- Modded scalers
- Single debug output node for any types 

# Nodes descriptions
- Debug output node
- Variables:
  - Float - mainly used to calculation
  - Integer - used to set width/height and offsets mainly, also provides converting of float values
  - Text - input field for text
  - Text box - same as text, but multiline
- Functional:
  - Random - gives random value within threshold
  - Get image size - return image size like: Width, Height
  - Get latent size - return latent size like: Width, Height
    - NOTE: Original values for latents are 8 times smaller
  - Logic node - compares 2 values and returns one of 2 others (if not set - returns False)
  - Converters: converts one type to another
    - Int to float
    - Ceil - rounding up float value ex: 1.01 --> 2
    - Floor - rounding down float value ex: 1.99 --> 1
    - Absolute - return only positive (or negative) value on your choice (default - positive)
- Math
  - sum - (A + B)
  - subtract - (A - B)
  - multiply (A * B)
  - divide - (A / B)
  - power - (A * A * A...) B times
  - square root - (√A)
- Modded:
  - Conditioning
    - Condition area scale - multiplies size of condion area
  - Latents
    - Latent scale by ratio - multiplies size of latent
    - Latent scale to size - scale size of latent to length of selected side
  - Image
    - Image scale by ratio - multiplies size of image
    - Image scale to size - scale size of image to length of selected side
