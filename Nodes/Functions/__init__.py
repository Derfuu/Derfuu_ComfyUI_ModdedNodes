import custom_nodes.Derfuu_ComfyUI_CustomNodes.Nodes.Functions.Converters as ConvNodes
import custom_nodes.Derfuu_ComfyUI_CustomNodes.Nodes.Functions.GetSizes as GetSizes
import custom_nodes.Derfuu_ComfyUI_CustomNodes.Nodes.Functions.Random as RendNodes
import custom_nodes.Derfuu_ComfyUI_CustomNodes.Nodes.Functions.Tuples as TupleNodes


NODE_CLASS_MAPPINGS = {
    "RandomFloat_DF": RendNodes.RandomValue,

    "Float2Tuple_DF": TupleNodes.Float2Tuple,
    "Tuple2Float_DF": TupleNodes.Tuple2Float,

    "Int2Float_DF": ConvNodes.Int2Float,
    "CeilNode_DF": ConvNodes.CeilNode,
    "FloorNode_DF": ConvNodes.FloorNode,
    "ABSNode_DF": ConvNodes.ABSNode,

    "GetLatentSize_DF": GetSizes.GetLatentSize,
    "GetImageSize_DF": GetSizes.GetImageSize,

}