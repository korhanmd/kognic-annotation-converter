class DetectedObject:
    object_id: str
    object_class: str
    optional_features: dict
    bbox: dict

    def __init__(self, object_id, object_class, optional_features):
        self.object_id = object_id
        self.object_class = object_class
        self.optional_features = optional_features
        self.bbox = {}

    def set_bbox(self, stream, bbox_coordinates):
        self.bbox[stream] = bbox_coordinates

    def get_id(self):
        return self.object_id

    def get_class(self):
        return self.object_class

    def get_bbox(self):
        return self.bbox

    def get_optional_features(self):
        return self.optional_features
