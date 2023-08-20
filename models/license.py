from enum import Enum


class License(str, Enum):
    # Variants.
    RF = "rf"
    RM = "rm"
    EITHER = 'either'

    def get_query_string(self) -> str:
        if self == License.RF:
            return "1"
        elif self == License.RM:
            return "2"
        else:
            return ""
