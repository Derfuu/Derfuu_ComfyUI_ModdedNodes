# Derfuu_ComfyUI_ModdedNodes

- **ComfyUI**: [LINK](https://github.com/comfyanonymous/ComfyUI)

## Small description
- Automate calculation depending on image sizes or something you want
- Easier(or not) editing multiple values of various nodes
- Math nodes
- Modded scalers (scale by side/ratio)
- String manipulations (Replace, Concat)
- Single debug output node for any types with widget 

# Nodes description
- Debug output node - tries to convert any input type into string and print it in widget and console.
- Variables:
  - Float - mainly used to calculation
  - Integer - used to set width/height and offsets mainly, also provides converting float values into integer
  - Text - input field for single line text
  - Text box - same as text, but multiline
  - DynamicPrompts Text Box - same as text box, but with standard dynamic prompts support (don't work when in-line)
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
    - Absolute - return only positive (or negative) value on your choice
  - String operations:
    - Concat - concatenates 2 strings (texts) separated with delimiter if you need one
    - Replace - replaces substring with other string
      - Strict mode - replace all occurrences of the pattern in the text with another string
      - RegEx mode - replace all occurrences of a pattern matching RegEx in the text with another string
- Math
  - sum - (A + B)
  - subtract - (A - B)
  - multiply (A * B)
  - divide - (A / B)
  - power - (A * A * A...) B times
  - square root - (√A)
- Modded:
  - Conditioning
    - Condition area scale - multiplies size of conditioning by ratio
  - Latents
    - Latent scale by ratio - multiplies size of latent by ratio
    - Latent scale to size - scale size of latent to length of selected side
  - Image
    - Image scale by ratio - multiplies size of image by ratio
    - Image scale to size - scale size of image to length of selected side
