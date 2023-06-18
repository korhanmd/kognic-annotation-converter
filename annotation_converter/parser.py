import json
from annotation_converter.detected_object import DetectedObject

def check_optional_features(object_features_dict):
    optional_features_dict = {}

    for key, value in object_features_dict.items():
        if key == "class":
            continue

        if isinstance(value, str):
            if "text" not in optional_features_dict:
                optional_features_dict["text"] = {}
            optional_features_dict["text"][key] = value
        elif isinstance(value, bool):
            if "boolean" not in optional_features_dict:
                optional_features_dict["boolean"] = {}
            optional_features_dict["boolean"][key] = value
        else:
            continue

    return optional_features_dict

def parse(file_name):
    objects_dict = {}

    with open(file_name, 'r', encoding="utf-8") as annotation_file:
        annotation_dict = json.load(annotation_file)
        for key in annotation_dict["shapeProperties"]:
            object_features_dict = annotation_dict["shapeProperties"][key]["@all"]
            optional_features_dict = check_optional_features(object_features_dict)
            detected_object = DetectedObject(key, object_features_dict["class"],
                                            optional_features_dict)
            objects_dict[key] = detected_object

        for stream in annotation_dict["shapes"]:
            for features in annotation_dict["shapes"][stream]["features"]:
                try:
                    current_object = objects_dict[features["id"]]
                except Exception:
                    print(f'There is no object with ID {features["id"]}')

                coordinate_format = features["geometry"]["type"]

                if coordinate_format == "ExtremePointBox":
                    bbox_coordinates = []
                    coordinates_dict = features["geometry"]["coordinates"]
                    bbox_coordinates.append(coordinates_dict["maxX"]["coordinates"])
                    bbox_coordinates.append(coordinates_dict["maxY"]["coordinates"])
                    bbox_coordinates.append(coordinates_dict["minX"]["coordinates"])
                    bbox_coordinates.append(coordinates_dict["minY"]["coordinates"])

                    current_object.set_bbox(stream, bbox_coordinates)
                else:
                    print(f'WARNING: {coordinate_format} coordinate format is not valid!')

    return objects_dict
