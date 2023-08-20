import xml.etree.ElementTree as ET

from pydantic.dataclasses import dataclasses

from models.image import Image
from utils.runners import run_in_executor


@dataclasses.dataclass
class Result:
    results: list[Image]

    @run_in_executor
    @staticmethod
    def from_xml_string(xml_string: str) -> 'Result':
        tree = ET.ElementTree(ET.fromstring(xml_string))
        return Result(results=[Image.from_element(x) for x in tree.iterfind('I')])
