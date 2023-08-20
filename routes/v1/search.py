import json
import time
from hashlib import sha256
from typing import Optional

from fastapi import status
from fastapi.responses import JSONResponse
from httpx import Client
from pydantic.dataclasses import dataclasses
from redis.asyncio import Redis

from config import logging
from models.license import License
from models.orientation import Orientation
from models.result import Result

client = Client(base_url="https://api.alamy.com")

redis = Redis(host="redis", port=6379)

_LOG = logging.getLogger("[search]")


async def search(
    query: str,
    orientation: Optional[Orientation] = Orientation.ALL,
    license: Optional[License] = License.EITHER,
    page_size: int = 1,
    page_number: int = 0,
    model_release: bool = False,
    property_release: bool = False,
) -> dict:
    _LOG.info(
        f"Request recieved for query {query}, ot: {orientation}, "
        f"lic: {license}, ps: {page_size}, pn: {page_number}",
    )

    start = time.perf_counter()
    # Prepare query parameters
    params = {
        'qt': query,
        'lic': license.get_query_string(),
    }
    if orientation != Orientation.ALL:
        params['ot'] = orientation.get_query_string()
    if model_release:
        params['mr'] = "1"
    if property_release:
        params['pr'] = "1"

    hash_string = sha256(":".join(map(str, params.values())).encode('utf-8')).hexdigest()

    result = await redis.get(hash_string)

    if result:
        print("cache hit")
        return json.loads(result)

    response = client.get('/images/api/v2/search', params=params)

    _LOG.info(f"Request for query {query} satisfied in {time.perf_counter()-start:.2f}s")
    if response.status_code >= 400:
        _LOG.error(
            f"Request for query {query} failed :- {response.text}",
            exc_info=True,
            stack_info=True,
        )
        raise JSONResponse(
            status_code=status.HTTP_502_BAD_GATEWAY,
            content={"message": "something went wrong"},
        )

    result = await Result.from_xml_string(response.text)
    data = dataclasses.asdict(result)

    await redis.set(hash_string, json.dumps(data), ex=30)

    return data
