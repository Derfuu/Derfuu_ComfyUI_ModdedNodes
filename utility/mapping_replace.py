import os
from json import load, dumps
from datetime import datetime

_mapping = {
    "Float": "DF_Float",
    "Integer": "DF_Integer",
    "Text": "DF_Text",
    "Text box": "DF_Text_Box",
    "String Concatenate": "DF_String_Concatenate",
    "String Replace": "DF_String_Replace",
    "To text (Debug)": "DF_To_text_(Debug)",
    "Random": "DF_Random",
    "Int to float": "DF_Int_to_Float",
    "Ceil": "DF_Ceil",
    "Floor": "DF_Floor",
    "Absolute value": "DF_Absolute_value",
    "Get latent size": "DF_Get_latent_size",
    "Get image size": "DF_Get_image_size",
    "Sum": "DF_Sum",
    "Subtract": "DF_Subtract",
    "Multiply": "DF_Multiply",
    "Divide": "DF_Divide",
    "Power": "DF_Power",
    "Square root": "DF_Square_root",
    "Sinus": "DF_Sinus",
    "Cosines": "DF_Cosines",
    "Tangent": "DF_Tangent",
    "Logic node": "DF_Logic_node",
    "Latent Scale by ratio": "DF_Latent_Scale_by_ratio",
    "Latent Scale to side": "DF_Latent_Scale_to_side",
    "Image scale by ratio": "DF_Image_scale_by_ratio",
    "Image scale to side": "DF_Image_scale_to_side",
    "Conditioning area scale by ratio": "DF_Conditioning_area_scale_by_ratio",
}

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
    print("Done.")
    input("Press any key to close console.")
