import custom_nodes.Derfuu_ComfyUI_CustomNodes.Nodes.Debug.debugNodes as DebugNodes

NODE_CLASS_MAPPINGS = {
    "FloatDebugPrint_DF": DebugNodes.DebugNodeFloat,
    "IntDebugPrint_DF": DebugNodes.DebugNodeInt,
    "TupleDebugPrint_DF": DebugNodes.DebugNodeTuple,
}