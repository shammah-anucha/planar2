# Without Docker

Install the Dependencies
poetry install

Start the server
poetry run uvicorn backend.app.app.main:app --reload


# Using Docker
## Build Docker image
docker build -t planar:1.0 .

## Run Container
docker run -t -p  8000:8000 planar:1.0

## To start container in yaml file
docker-compose -f docker-compose.yml up 
docker compose up

## To stop container in yaml file
docker-compose -f docker-compose.yml down or Ctrl+C