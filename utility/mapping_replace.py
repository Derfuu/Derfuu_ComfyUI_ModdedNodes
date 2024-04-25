import os
from json import load, dumps
from datetime import datetime

_new_mapping = [
    "DF_Float",
    "DF_Integer",
    "DF_Text",
    "DF_Text_Box",
    "DF_String_Concatenate",
    "DF_String_Replace",
    "DF_To_text_(Debug)",
    "DF_Random",
    "DF_Int_to_Float",
    "DF_Ceil",
    "DF_Floor",
    "DF_Absolute_value",
    "DF_Get_latent_size",
    "DF_Get_image_size",
    "DF_Sum",
    "DF_Subtract",
    "DF_Multiply",
    "DF_Divide",
    "DF_Power",
    "DF_Square_root",
    "DF_Sinus",
    "DF_Cosines",
    "DF_Tangent",
    "DF_Logic_node",
    "DF_Latent_Scale_by_ratio",
    "DF_Latent_Scale_to_side",
    "DF_Image_scale_by_ratio",
    "DF_Image_scale_to_side",
    "DF_Conditioning_area_scale_by_ratio",
]
_old_mapping = [
    "Float",
    "Integer",
    "Text",
    "Text box",
    "String Concatenate",
    "String Replace",
    "To text (Debug)",
    "Random",
    "Int to float",
    "Ceil",
    "Floor",
    "Absolute value",
    "Get latent size",
    "Get image size",
    "Sum",
    "Subtract",
    "Multiply",
    "Divide",
    "Power",
    "Square root",
    "Sinus",
    "Cosines",
    "Tangent",
    "Logic node",
    "Latent Scale by ratio",
    "Latent Scale to side",
    "Image scale by ratio",
    "Image scale to side",
    "Conditioning area scale by ratio",
]
_mapping = {_old_mapping[ix]: new_name for ix, new_name in enumerate(_new_mapping)}

if __name__ == "__main__":
    json_file = input("workflow.json where replace mappings: ")
    with open(json_file, "r") as j_file:
        workflow = load(j_file)

    for node in workflow["nodes"]:
        print(node["type"], end=" -> ")
        if node["type"] in _mapping.keys():
            node["type"] = _mapping[node["type"]]
        print(node["type"])

    replaced_folder = "replaced"
    if replaced_folder not in os.listdir(os.curdir):
        os.mkdir(replaced_folder)
    path = f"{replaced_folder}/{datetime.now().strftime('%d-%m-%Y %H.%M.%S')}.json"
    with open(path, "w") as j_file:
        j_file.write(dumps(workflow))
