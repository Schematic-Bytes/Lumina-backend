from enum import Enum


class Orientation(str, Enum):
    # Variants.
    LANDSCAPE = "landscape"
    PORTRAIT = "portrait"
    PANORAMIC = "panoramic"
    SQUARE = "square"
    ALL = "all"
    # Internal mapping to the alamy API orientation reprsentation.
    __MAPPING__ = {"landscape": 1, "portrait": 2, "panoramic": 4, "square": 8}

    def get_query_string(self) -> str:
        if self == Orientation.ALL:
            return ""
        else:
            return f"{self.__MAPPING__[self.value]}"
