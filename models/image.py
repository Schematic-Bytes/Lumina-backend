from xml.etree.ElementTree import Element

from pydantic.dataclasses import dataclasses

THUMB_BASE_URL = "https://c7.alamy.com/zooms/3/"
BASE_URL = "https://c7.alamy.com/comb/"


@dataclasses.dataclass
class Image:
    id: str

    filename: str
    caption: str

    mr: int
    pr: int

    @staticmethod
    def from_element(element: Element) -> 'Image':
        return Image(
            id=element.get('ID').strip("{}"),
            filename=element.get('AR'),
            caption=element.get('CAPTION'),
            mr=int(element.get('MR')),
            pr=int(element.get('PR')),
        )

    @property
    def thumbnail_url(self) -> str:
        return f"{THUMB_BASE_URL}{self.id}/{self.filename}.jpg"
