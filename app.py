from fastapi import FastAPI
from fastapi.middleware.gzip import GZipMiddleware

from routes.v1.image_search import image_reverse_lookup
from routes.v1.search import search

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "The server is running"}


# Add middlewares
app.add_middleware(GZipMiddleware, minimum_size=500)
# Add API routes
app.add_api_route("/api/v1/search/", methods=['GET'], endpoint=search)
app.add_api_route("/api/v1/search/{query}", methods=['GET'], endpoint=search)
app.add_api_route("/api/v1/reverse_lookup/", methods=['POST'], endpoint=image_reverse_lookup)
