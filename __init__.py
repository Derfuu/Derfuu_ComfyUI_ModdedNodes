import custom_nodes.Derfuu_ComfyUI_ModdedNodes.Nodes.Custom.Types as TypeNodes

import custom_nodes.Derfuu_ComfyUI_ModdedNodes.Nodes.Debug.Debug as DebugNodes

import custom_nodes.Derfuu_ComfyUI_ModdedNodes.Nodes.Functions.Converters as ConvNodes
import custom_nodes.Derfuu_ComfyUI_ModdedNodes.Nodes.Functions.GetSizes as GetSizes
import custom_nodes.Derfuu_ComfyUI_ModdedNodes.Nodes.Functions.Random as RandNodes
import custom_nodes.Derfuu_ComfyUI_ModdedNodes.Nodes.Functions.Tuples as TupleNodes

import custom_nodes.Derfuu_ComfyUI_ModdedNodes.Nodes.Math.SimpleMath as SMath
import custom_nodes.Derfuu_ComfyUI_ModdedNodes.Nodes.Math.Trigonometry as TMath

import custom_nodes.Derfuu_ComfyUI_ModdedNodes.Nodes.Modded.Images as ImageNodes
import custom_nodes.Derfuu_ComfyUI_ModdedNodes.Nodes.Modded.Latents as LatentNodes
import custom_nodes.Derfuu_ComfyUI_ModdedNodes.Nodes.Modded.Condotionig as CondNodes

NODE_CLASS_MAPPINGS = {
    "FloatNode_DF": TypeNodes.FloatNode,
    "IntegerNode_DF": TypeNodes.IntegerNode,
    "StringNode_DF": TypeNodes.StringNode,
    "TupleNode_DF": TypeNodes.TupleNode,
    "MultilineStringNode_DF": TypeNodes.MultilineStringNode,

    "FloatDebugPrint_DF": DebugNodes.DebugNodeFloat,
    "IntDebugPrint_DF": DebugNodes.DebugNodeInt,
    "TupleDebugPrint_DF": DebugNodes.DebugNodeTuple,

    "RandomFloat_DF": RandNodes.RandomValue,

    "Float2Tuple_DF": TupleNodes.Float2Tuple,
    "FlipTuple_DF": TupleNodes.FlipTuple,
    "Tuple2Float_DF": TupleNodes.Tuple2Float,
    "Tuple2Int_DF": TupleNodes.Tuple2Int,

    "Int2Float_DF": ConvNodes.Int2Float,
    "CeilNode_DF": ConvNodes.CeilNode,
    "FloorNode_DF": ConvNodes.FloorNode,
    "ABSNode_DF": ConvNodes.ABSNode,

    "GetLatentSize_DF": GetSizes.GetLatentSize,
    "GetImageSize_DF": GetSizes.GetImageSize,

    "SumNode_DF": SMath.SumNode,
    "SubtractNode_DF": SMath.SubtractNode,
    "MultiplyNode_DF": SMath.MultiplyNode,
    "DivideNode_DF": SMath.DivideNode,
    "PowNode_DF": SMath.PowNode,
    "SqrtNode_DF": SMath.SquareRootNode,

    "SinNode_DF": TMath.SinNode,
    "CosNode_DF": TMath.CosNode,
    "TanNode_DF": TMath.tgNode,

    # "EmptyLatentImage_DF": LatentNodes.EmptyLatentImage,
    "LatentScale_Ratio_DF": LatentNodes.LatentScale_Ratio,
    "LatentScale_Side_DF": LatentNodes.LatentScale_Side,
    # "LatentComposite_DF": LatentNodes.LatentComposite,

    "ImageScale_Ratio_DF": ImageNodes.ImageScale_Ratio,
    "ImageScale_Side_DF": ImageNodes.ImageScale_Side,

    "ConditioningSetArea_DF": CondNodes.ConditioningSetArea_MOD,
    # "ConditioningSetAreaEXT_DF": CondNodes.ConditioningSetAreaExt_MOD,
}
