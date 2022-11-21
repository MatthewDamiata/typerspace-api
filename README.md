[![Coverage Status](https://coveralls.io/repos/github/MatthewDamiata/typerspace-api/badge.svg?branch=main)](https://coveralls.io/github/MatthewDamiata/typerspace-api?branch=main)

# API for [typerspace](https://github.com/benjaminlapidus/typerspace), built with FastAPI

## What is Typerspace?
Typerspace lets users practice their typing skills by following along with the captions to a YouTube video.

## Installation

1. Clone the repository.
2. Install [Poetry](https://python-poetry.org/).
2. Install [Python 3.10.4](https://www.python.org/downloads/release/python-3104/).
3. Run `./typerspace install` to install the dependencies.

## Tests

Run `./typerspace test` to run the tests.

## Running the server

Run `./typerspace service` to run the server.
> This is only for development purposes, production is not supported yet.

## OpenAPI

To view the docs, run the server and go to `http://127.0.0.1:8000/docs`.

## Contributing

1. Fork the repository.
2. Create a new branch.
3. Install the dependencies with `./typerspace install`.
3. Make your changes.
4. Run `./typerspace test` and `./typerspace checks`.
6. Submit a pull request.
