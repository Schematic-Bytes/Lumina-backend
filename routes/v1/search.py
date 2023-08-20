import time
from typing import Optional

from fastapi import status
from fastapi.responses import JSONResponse
from httpx import Client
from pydantic.dataclasses import dataclasses

from config import logging
from models.license import License
from models.orientation import Orientation
from models.result import Result

client = Client(base_url="https://api.alamy.com")

_LOG = logging.getLogger("[search]")


async def search(
    query: str,
    orientation: Optional[Orientation] = Orientation.ALL,
    license: Optional[License] = License.EITHER,
    page_size: int = 1,
    page_number: int = 0,
) -> dict:
    _LOG.info(
        f"Request recieved for query {query}, ot: {orientation}, "
        f"lic: {license}, ps: {page_size}, pn: {page_number}",
    )
    start = time.perf_counter()
    response = client.get(
        '/images/api/v2/search',
        params={
            'qt': query,
            'ot': orientation.get_query_string(),
            'lic': license.get_query_string(),
        },
    )
    _LOG.info(f"Request for query {query} satisfied in {time.perf_counter()-start:.2f}s")
    if response.status_code >= 400:
        _LOG.error(f"Request for query {query} failed :- {response.text}", exc_info=True, stack_info=True)
        raise JSONResponse(status_code=status.HTTP_502_BAD_GATEWAY, content={"message": "something went wrong"})

    result = await Result.from_xml_string(response.text)

    return dataclasses.asdict(result)
