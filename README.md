# fastapi-list-pagination
A POC for pagination of a hardcorded list on FastAPI.

###

This is a simple proof-of-concept to "paginate" a hardcoded list on a Python server, using FastAPI as a web framework.

The idea is to generate an integer list and return a sublist based on query parameters received at an endpoint. In this POC, the `limit` and `page` parameters are used on a `/range` endpoint.

The list is subdivided into chunks with size defined by the `limit` param. We then select the chunk at the index defined by the `page` parameter, accounting for the 0-index.  Finally, a JSON response is returned with the following structure:

```json
{
	"contents": [
		0,
		1,
		2,
		3,
		4,
		5,
		6,
		7,
		8,
		9
	],
	"current_page": 1,
	"pages": 100,
	"limit": 10
}
```

Where:
- We request the endpoint with `range?limit=10&page=1`.
- `contents` is the chunk positioned according to the `page` parameter, or its position on the chunk list accounting for the 0 index.
- `current_page` is the original `page` parameter, used to navigate between chunks.
- `pages` is the total number of chunks, considering the chunk size defined by the `limit` parameter.
- `limit` is the original `limit` parameter used to subdivide the list.

By passing other integers on the `page` parameter, we are able to traverse to the next chunks. Requesting a page higher than the total page count will return the last page available. By changing the `limit` parameter, we are able to control the chunk size and thus modify the `pages` count and the `contetns` length.

You may also control the list size, or even experiment with other data structures by modifying the `generate_list` function in the `core/assets.py` file.

## Installation

This project originally uses [pyenv](https://github.com/pyenv/pyenv) to set up a Python 3.9.10 application environment:

```bash
pyenv install 3.9.10
pyenv virtualenv 3.9.10 fastapi-list-pagination-env
pyenv exec pip install -r requirements.txt 
```

## Running locally

To run the API on your local machine, simply activate the virtual environment and run uvicorn:

```bash
pyenv activate fastapi-list-pagination-env
uvicorn main:app --reload
```
