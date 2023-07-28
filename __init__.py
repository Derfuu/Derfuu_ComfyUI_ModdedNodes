import custom_nodes.Derfuu_ComfyUI_ModdedNodes.Nodes.Custom.Types as TypeNodes

import custom_nodes.Derfuu_ComfyUI_ModdedNodes.Nodes.Debug.Debug as DebugNodes

import custom_nodes.Derfuu_ComfyUI_ModdedNodes.Nodes.Functions.Converters as ConvNodes
import custom_nodes.Derfuu_ComfyUI_ModdedNodes.Nodes.Functions.GetSizes as GetSizes
import custom_nodes.Derfuu_ComfyUI_ModdedNodes.Nodes.Functions.Random as RandNodes
import custom_nodes.Derfuu_ComfyUI_ModdedNodes.Nodes.Functions.Tuples as TupleNodes

import custom_nodes.Derfuu_ComfyUI_ModdedNodes.Nodes.Math.SimpleMath as SMath
import custom_nodes.Derfuu_ComfyUI_ModdedNodes.Nodes.Math.Trigonometry as TMath

import custom_nodes.Derfuu_ComfyUI_ModdedNodes.Nodes.Modded.StandardInputs.Images as St_ImageNodes
import custom_nodes.Derfuu_ComfyUI_ModdedNodes.Nodes.Modded.StandardInputs.Latents as St_LatentNodes
import custom_nodes.Derfuu_ComfyUI_ModdedNodes.Nodes.Modded.StandardInputs.Condotionig as St_CondNodes

import custom_nodes.Derfuu_ComfyUI_ModdedNodes.Nodes.Modded.TuplesUsed.Latents as Tu_LatentNodes
import custom_nodes.Derfuu_ComfyUI_ModdedNodes.Nodes.Modded.TuplesUsed.Conditioning as Tu_CondNodes


NODE_CLASS_MAPPINGS = {
    "Float": TypeNodes.FloatNode,                               # Return float Value
    "Integer": TypeNodes.IntegerNode,                           # Return int Value
    "Text": TypeNodes.StringNode,                               # IDK where to use this... yet
    "Text box": TypeNodes.MultilineStringNode,                  # This too

    # NOTE: if input values are not changed, they don't print in console, same to random IDK how to fix this yet
    "Float debug print": DebugNodes.DebugNodeFloat,
    "Int debug print": DebugNodes.DebugNodeInt,
    "Tuple debug print": DebugNodes.DebugNodeTuple,
    "String debug print": DebugNodes.DebugNodeString,

    "Random": RandNodes.RandomValue,                            # Return random value in range

    "Tuple": TupleNodes.Tuple,                                  # Takes floats into Tuple
    "Int to tuple": TupleNodes.Int2Tuple,                       # Takes ints into Tuple
    "Tuple to floats": TupleNodes.Tuple2Float,                  # Return 2 floats from Tuple
    "Tuple to ints": TupleNodes.Tuple2Int,                      # Return 2 ints from Tuple
    "Tuple swap": TupleNodes.FlipTuple,                         # Swap Values in tuple
    "Tuple multiply": TupleNodes.MultiplyTupleBy,

    "Int to float": ConvNodes.Int2Float,                        # Interpretation of int value as float
    "Ceil": ConvNodes.CeilNode,                                 # Rounds Value to next int
    "Floor": ConvNodes.FloorNode,                               # Rounds Value to previous int
    "Absolute value": ConvNodes.ABSNode,                        # Return absolute Value of input

    "Get latent size": GetSizes.GetLatentSize,                  # Return size of latent
    "Get image size": GetSizes.GetImageSize,                    # Return size of image

    "Sum": SMath.SumNode,                                       # Summaries 2 values
    "Subtract": SMath.SubtractNode,                             # Subtracts Value_B from Value_A
    "Multiply": SMath.MultiplyNode,                             # Multiplies 2 values
    "Divide": SMath.DivideNode,                                 # Divides Value_A on Value_B
    "Power": SMath.PowNode,                                     # Returns Value_A powered by Value_B
    "Square root": SMath.SquareRootNode,                        # Returns square root of Value

    "Sinus": TMath.SinNode,                                     # Returns sinus of Value
    "Cosines": TMath.CosNode,                                   # Returns cosines of Value
    "Tangent": TMath.tgNode,                                    # Returns tangents of Value


    # STANDARD MODDED
    "Latent Scale by ratio": St_LatentNodes.LatentScale_Ratio,     # Scales latent proportionally on value
    "Latent Scale to side": St_LatentNodes.LatentScale_Side,       # Proportionally scales latent to fit in side size
    "Image scale by ratio": St_ImageNodes.ImageScale_Ratio,        # Scales image proportionally on value
    "Image scale to side": St_ImageNodes.ImageScale_Side,          # Proportionally scales image to fit in side size
    "Conditioning area scale by ratio": St_CondNodes.ConditioningAreaScale_Ratio,


    # TUPLE MODDED
    "ConditioningSetArea with tuples": Tu_CondNodes.ConditioningSetArea,     # Compose condition on field using tuples
    "LatentComposite with tuples": Tu_LatentNodes.LatentComposite,
}
