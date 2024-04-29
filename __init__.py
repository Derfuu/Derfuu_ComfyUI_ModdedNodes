"""
@author: Derfuu
@title: Derfuu simple/modded Nodes
@nickname: Derfuu simple/modded Nodes
@description: Pack of simple (or not) and modded nodes for scaling images/latents, editing numbers or text. Automate calculations depending on image sizes or any other thing you want. Or randomize any number in your workflow. Debug node included.
"""

from .pyscripts.Nodes.Custom import Types as TypeNodes

from .pyscripts.Nodes.Debug import Debug as DebugNodes

from .pyscripts.Nodes.Functions import Converters as ConvNodes
from .pyscripts.Nodes.Functions import GetSizes as GetSizes
from .pyscripts.Nodes.Functions import Random as RandNodes
from .pyscripts.Nodes.Functions import Strings as StringNodes

from .pyscripts.Nodes.Math import SimpleMath as SMath
from .pyscripts.Nodes.Math import Trigonometry as TMath

from .pyscripts.Nodes.Custom import LogicNode as LNode

from .pyscripts.Nodes.Modded import Images as St_ImageNodes
from .pyscripts.Nodes.Modded import Latents as St_LatentNodes
from .pyscripts.Nodes.Modded import Conditioning as St_CondNodes


_ident = "DF_"
_n = lambda name: f"{_ident}{name}"

NODE_CLASS_MAPPINGS = {
    _n("Float"): TypeNodes.FloatNode,
    _n("Integer"): TypeNodes.IntegerNode,
    _n("Text"): TypeNodes.StringNode,
    _n("Text_Box"): TypeNodes.MultilineStringNode,
    _n("DynamicPrompts_Text_Box"): TypeNodes.AsDynamicPromptsStringNode,
    _n("String_Concatenate"): StringNodes.StringConcat,
    _n("String_Replace"): StringNodes.StringReplace,
    _n("To_text_(Debug)"): DebugNodes.ShowDataDebug,
    _n("Random"): RandNodes.RandomValue,
    _n("Int_to_Float"): ConvNodes.Int2Float,
    _n("Ceil"): ConvNodes.CeilNode,
    _n("Floor"): ConvNodes.FloorNode,
    _n("Absolute_value"): ConvNodes.ABSNode,
    _n("Get_latent_size"): GetSizes.GetLatentSize,
    _n("Get_image_size"): GetSizes.GetImageSize,
    _n("Sum"): SMath.SumNode,
    _n("Subtract"): SMath.SubtractNode,
    _n("Multiply"): SMath.MultiplyNode,
    _n("Divide"): SMath.DivideNode,
    _n("Power"): SMath.PowNode,
    _n("Square_root"): SMath.SquareRootNode,
    _n("Sinus"): TMath.SinNode,
    _n("Cosines"): TMath.CosNode,
    _n("Tangent"): TMath.tgNode,
    _n("Logic_node"): LNode.LogicNode,
    _n("Latent_Scale_by_ratio"): St_LatentNodes.LatentScale_Ratio,
    _n("Latent_Scale_to_side"): St_LatentNodes.LatentScale_Side,
    _n("Image_scale_by_ratio"): St_ImageNodes.ImageScale_Ratio,
    _n("Image_scale_to_side"): St_ImageNodes.ImageScale_Side,
    _n("Conditioning_area_scale_by_ratio"): St_CondNodes.ConditioningAreaScale_Ratio,
}

WEB_DIRECTORY = "./scripts"
NODE_DISPLAY_NAME_MAPPINGS = {k: k.replace(_ident, "").replace("_", " ") for k in NODE_CLASS_MAPPINGS}

__all__ = ["NODE_CLASS_MAPPINGS", "WEB_DIRECTORY"]
