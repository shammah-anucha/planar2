poetry install

<!-- poetry run uvicorn api.main:app --reload -->

poetry run uvicorn backend.app.app.main:app --reload


# docker run -p 8000:8000 planar
docker run -d -p  8000:8000 planar:1.0