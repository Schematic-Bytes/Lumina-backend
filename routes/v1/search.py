from typing import Optional

from fastapi import status
from fastapi.responses import JSONResponse
from httpx import Client
from pydantic.dataclasses import dataclasses

from models.license import License
from models.orientation import Orientation
from models.result import Result

client = Client(base_url="https://api.alamy.com")


async def search(
    query: str,
    orientation: Optional[Orientation] = Orientation.ALL,
    license: Optional[License] = License.EITHER,
    page_size: int = 1,
    page_number: int = 0,
) -> dict:
    response = client.get(
        '/images/api/v2/search',
        params={
            'qt': query,
            'ot': orientation.get_query_string(),
            'lic': license.get_query_string(),
        },
    )
    if response.status_code >= 400:
        raise JSONResponse(status_code=status.HTTP_502_BAD_GATEWAY, content={"message": "something went wrong"})

    result = await Result.from_xml_string(response.text)

    return dataclasses.asdict(result)
