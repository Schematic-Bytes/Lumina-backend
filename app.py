from fastapi import FastAPI
from fastapi.middleware.gzip import GZipMiddleware

from routes.v1.search import search

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "The server is running"}


app.add_middleware(GZipMiddleware, minimum_size=500)
app.add_api_route("/api/v1/search/", endpoint=search)
app.add_api_route("/api/v1/search/{query}", endpoint=search)
