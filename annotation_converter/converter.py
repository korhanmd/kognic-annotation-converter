from annotation_converter.parser import parse
from annotation_converter.calculator import calculate_coordinates

def get_objects(objects_dict):
    open_label_objects_dict = {}

    for object_id, detected_object in objects_dict.items():
        info_dict = {}
        info_dict["name"] = detected_object.get_id()
        info_dict["type"] = detected_object.get_class()
        open_label_objects_dict[object_id] = info_dict

    return open_label_objects_dict

def get_optional_features_list(optional_feature, optional_features):
    try:
        selected_optional_features = optional_features[optional_feature]
        optional_features_list = []

        for feature_name, feature_value in selected_optional_features.items():
            optional_feature_dict = {}
            optional_feature_dict["name"] = feature_name
            optional_feature_dict["val"] = feature_value
            optional_features_list.append(optional_feature_dict)

        return optional_features_list
    except Exception:
        return None

def get_frames(objects_dict):
    open_label_frames_dict = {}

    for object_id, detected_object in objects_dict.items():
        object_data_dict = {}
        bbox_list = []

        for stream, coordinates in detected_object.get_bbox().items():
            bbox_dict = {}

            bbox_name = "bbox-" + object_id.split('-')[0]
            open_label_coords = calculate_coordinates(coordinates)

            bbox_dict["name"] = bbox_name
            bbox_dict["stream"] = stream
            bbox_dict["val"] = open_label_coords

            bbox_list.append(bbox_dict)

        object_data_dict["bbox"] = bbox_list

        optional_features = detected_object.get_optional_features()

        bool_features_list = get_optional_features_list("boolean", optional_features)
        if bool_features_list is not None:
            object_data_dict["boolean"] = bool_features_list

        text_features_list = get_optional_features_list("text", optional_features)
        if text_features_list is not None:
            object_data_dict["text"] = text_features_list

        open_label_frames_dict[object_id] = {"object_data": object_data_dict}

    return open_label_frames_dict

def convert(file_name):
    # Parse the json file in Kognic format
    # Create a dictionary of detected objects
    objects_dict = parse(file_name)

    # Use the dictionary of detected objects
    # Create dictionary as the value of "objects" key in Open Label json
    open_label_objects_dict = get_objects(objects_dict)

    # Use the dictionary of detected objects
    # Create dictionary as the value of "objects" key under "frames" in Open Label json
    open_label_frames_dict = get_frames(objects_dict)

    # Merge all dictionaries into Open Label format to create final dictionary
    open_label_dict = {"data":
                       {"openlabel":
                        {"objects": open_label_objects_dict,
                         "frames":
                         {"0":
                          {"objects": open_label_frames_dict}}}}}

    return open_label_dict
