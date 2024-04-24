from .pyscripts.Nodes.Custom import Types as TypeNodes

from .pyscripts.Nodes.Debug import Debug as DebugNodes

from .pyscripts.Nodes.Functions import Converters as ConvNodes
from .pyscripts.Nodes.Functions import GetSizes as GetSizes
from .pyscripts.Nodes.Functions import Random as RandNodes
from .pyscripts.Nodes.Functions import Tuples as TupleNodes
from .pyscripts.Nodes.Functions import Strings as StringNodes

from .pyscripts.Nodes.Math import SimpleMath as SMath
from .pyscripts.Nodes.Math import Trigonometry as TMath

from .pyscripts.Nodes.Custom import LogicNode as LNode

from .pyscripts.Nodes.Modded.StandardInputs import Images as St_ImageNodes
from .pyscripts.Nodes.Modded.StandardInputs import Latents as St_LatentNodes
from .pyscripts.Nodes.Modded.StandardInputs import Condotionig as St_CondNodes


WEB_DIRECTORY = "./scripts"

NODE_CLASS_MAPPINGS = {
    "Float": TypeNodes.FloatNode,                   # Return float Value
    "Integer": TypeNodes.IntegerNode,               # Return int Value
    "Text": TypeNodes.StringNode,                   # IDK where to use this... yet
    "Text box": TypeNodes.MultilineStringNode,      # This too

    "String Concatenate": StringNodes.StringConcat,  # Concat 2 strings into single one with delimiter between them
    "String Replace": StringNodes.StringReplace,     # Replaces substring in main string with new one.

    # NOTE: if input values are not changed, they don't print in console
    # thanks for solution from pythongosssss and Suzie1 to usage of "any" input type for nodes
    "To text (Debug)": DebugNodes.ShowDataDebug,    # Return any converted into string if possible

    "Random": RandNodes.RandomValue,                # Return random value in range

    "Int to float": ConvNodes.Int2Float,            # Interpretation of int value as float
    "Ceil": ConvNodes.CeilNode,                     # Rounds Value to next int
    "Floor": ConvNodes.FloorNode,                   # Rounds Value to previous int
    "Absolute value": ConvNodes.ABSNode,            # Return absolute Value of input

    "Get latent size": GetSizes.GetLatentSize,      # Return size of latent
    "Get image size": GetSizes.GetImageSize,        # Return size of image

    "Sum": SMath.SumNode,                           # Summaries 2 values
    "Subtract": SMath.SubtractNode,                 # Subtracts Value_B from Value_A
    "Multiply": SMath.MultiplyNode,                 # Multiplies 2 values
    "Divide": SMath.DivideNode,                     # Divides Value_A on Value_B
    "Power": SMath.PowNode,                         # Returns Value_A powered by Value_B
    "Square root": SMath.SquareRootNode,            # Returns square root of Value

    "Sinus": TMath.SinNode,                         # Returns sinus of Value
    "Cosines": TMath.CosNode,                       # Returns cosines of Value
    "Tangent": TMath.tgNode,                        # Returns tangents of Value

    # LOGIC (???)
    "Logic node": LNode.LogicNode,

    # STANDARD MODDED
    "Latent Scale by ratio": St_LatentNodes.LatentScale_Ratio,     # Scales latent proportionally on value
    "Latent Scale to side": St_LatentNodes.LatentScale_Side,       # Proportionally scales latent to fit in side size
    "Image scale by ratio": St_ImageNodes.ImageScale_Ratio,        # Scales image proportionally on value
    "Image scale to side": St_ImageNodes.ImageScale_Side,          # Proportionally scales image to fit in side size
    "Conditioning area scale by ratio": St_CondNodes.ConditioningAreaScale_Ratio,
}
