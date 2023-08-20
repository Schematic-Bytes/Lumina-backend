from xml.etree.ElementTree import Element

from pydantic.dataclasses import dataclasses

THUMB_BASE_URL = "https://c7.alamy.com/zooms/9/"
BASE_URL = "https://c7.alamy.com/comb/"


@dataclasses.dataclass
class Image:
    id: str

    filename: str
    caption: str

    mr: int
    pr: int

    thumbnail_url: str

    @staticmethod
    def from_element(element: Element) -> 'Image':
        id = element.get('ID').strip("{}")
        filename = element.get('AR')
        return Image(
            id=id,
            filename=filename,
            caption=element.get('CAPTION'),
            mr=int(element.get('MR')),
            pr=int(element.get('PR')),
            thumbnail_url=Image.thumbnail_url(id=id, filename=filename),
        )

    @staticmethod
    def thumbnail_url(id: str, filename: str) -> str:
        return f"{THUMB_BASE_URL}{id}/{filename}.jpg"
