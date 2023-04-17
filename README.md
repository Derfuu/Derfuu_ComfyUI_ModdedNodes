# Derfuu_ComfyUI_ModdedNodes

- **ComfyUI**: [LINK](https://github.com/comfyanonymous/ComfyUI)
- **CivitAI post**: [LINK](https://civitai.com/models/21558/comfyui-derfuu-math-and-modded-nodes)

## Small description
- Automate calculation depending on image sizes or something you want
- easier(or not) editing multiple values of various nodes
- Math
- Modded scalers

## Used:
- model: hPANTYHOSENEKO (can't find link, sorry) <_<
- vae: kl-f8-anime2
- embedding: [verybadimagenegative-6400](https://civitai.com/models/11772/verybadimagenegative)

# Previews:
- Only composed latents:
![compose_only](https://user-images.githubusercontent.com/54149748/228344136-505dfd42-7e43-4a38-aa35-ec41f811d8ae.png)

- Composed latents with area modifiers:
![with_set_areas](https://user-images.githubusercontent.com/54149748/228344160-e84ebb1f-a732-4dc6-98d7-f3ede5671850.png)

- All included nodes:
![all_nodes](https://user-images.githubusercontent.com/54149748/228344526-61653a0d-499a-41de-9a97-7f612117477d.png)

## Workflow example:
![workflow_preview](https://user-images.githubusercontent.com/54149748/228344751-616b0198-3855-4212-98a1-0fe5004dfa01.png)

# Nodes descriptions
- Variables:
  - Float - mainly used to calculation
  - Integer - used to set width/height and offsets mainly, also provides converting of float values
  - Text - input field for text
  - Text box - same, but multiline
- Debug nodes: **prints values in console**
  - DebugFloat
  - DebugInt
  - DebugText
  - DebugTuple
- Functional:
  - Random - gives random value within threshold
  - Get image size - return image size like: Width, Height and (Width, Height) in one value as tuple
  - Get latent size - return latent size like: Width, Height and (Width, Height) in one value as tuple
    - NOTE: Original values are 8 times smaller
  - Converters: converts one type to another
    - Int to float
    - Ceil - rounding up float value ex: 1.01 --> 2
    - Floor - rounding down float value ex: 1.99 --> 1
    - Absolute - return only positive (or negative) value on your choice (default - positive)
- Tuples (dead fetch?)
- Maths
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
    - Image scale by ratio - multiplies size of latent
    - Image scale to size - scale size of image to length of selected side
