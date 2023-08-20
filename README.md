## Lumina Backend: Proxy Microservice for Alamy Image Search API

Lumina Backend is a backend server created using FastAPI, designed to serve as a powerful proxy microservice for the Alamy API server. The Alamy API provides access to an image search API, allowing you to search for high-quality images. Lumina Backend enhances this experience by providing user-friendly filtering, pagination capabilities, and a unique reverse image lookup feature that labels objects.

## Table of Contents

- Introduction
- Features
- Getting Started
    - Prerequisites
    - Installation and Setup
    - Configuration
- Usage
- API Endpoints
- Reverse Image Lookup
- Contributing
- License

### Introduction

Lumina Backend acts as an intermediary layer between your application and the Alamy API server. It streamlines the process of interacting with the Alamy API by providing advanced filtering, pagination capabilities, and an innovative reverse image lookup feature. Built with FastAPI, Lumina Backend offers high performance and reliability.
Features

- - *__Proxy Microservice__*: Lumina Backend efficiently handles communication with the Alamy API server on behalf of your application.

- *__User-Friendly Filtering__*: Easily apply filters to your image searches, making it simple to narrow down results based on keywords, categories, and more.

- *__Pagination__*: Lumina Backend supports pagination, ensuring that large search result sets are returned in manageable chunks for improved performance.

- *__Reverse Image Lookup__*: A standout feature of Lumina Backend is the reverse image lookup capability, powered by the YOLOv8 Detection model. Submit an image, and Lumina Backend will utilize the YOLOv8 Detection model to accurately label objects detected in the image, providing you with additional context and valuable insights.

- *__Security__*: Lumina Backend ensures secure communication between your application and the Alamy API, helping you maintain the privacy and integrity of your data.

### Getting Started
#### Prerequisites

Before setting up Lumina Backend, ensure you have the following prerequisites:

    Python (version 3.9+)
    Pip (Python package manager)
    Docker (version 23+)


__Installation and Setup__

Clone this repository to your local machine:

```bash
git clone https://github.com/Schematic-Bytes/Lumina-backend
```
Navigate to the project directory:

`cd Lumina-backend`

Run inside the docker:

`docker-compose up -d`

Development usage:

Start Lumina Backend server:

`uvicorn app:app --reload`

Access the API endpoints using a web browser or API client. Refer to the API Endpoints section for details on available endpoints and their usage.

## API Endpoints

Lumina Backend exposes the following API endpoints:

`GET /api/v1/search/`: Perform an image search using the Alamy API with user-friendly filtering and pagination.

`POST /api/v1/reverse_lookup/`: Submit an image for reverse image lookup, retrieving labeled object information.

Refer to the API documentation within the codebase for detailed endpoint descriptions and usage instructions.
Reverse Image Lookup

The reverse image lookup feature offers a unique way to gain insights from images. Submit an image using the /reverse-lookup endpoint to receive information about objects detected in the image.
Contributing

## License

Lumina Backend is an open-source project licensed under the MIT License. You have the freedom to use, modify, and distribute this software according to the terms of the license.
