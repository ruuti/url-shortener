# URL shortener

## Introduction

"url-shortener" is a URL shortener system that generates a shorter version of a user inputted link. ADRs can be found [here](/docs/architecture-decisions).

## Architecture

This system is separated into three different Lambda functions:
* HTTP POST /: accepts POST request with JSON data containing a link to be shortneted
* HTTP GET /{id}: accepts GET request with an id. It returns an object containing a full link to orignial destination.
* Count (not implemented): listens SQS and inserts counts to db

![Architecture](architecture.png?raw=true "System overview")

## Usage

### Create a short link

To start env see [Development](#Development).

```
curl -X POST \
-H 'Content-Type: application/json' \
-d '{"url":"https://url.com"}' \
http://localhost:8000/
```

Example response:

```
{
  "id": "7c2a990e",
  "url": "https://url.com",
  "short_link": "https://localhost:8000/7c2a990e"
}
```

### Get full link by id

To start env see [Development](#Development).

```
curl -X GET http://localhost:8000/7c2a990e
```

Example response:
```
{
  "id": "7c2a990e",
  "url": "https://url.com",
  "short_link": "https://localhost:8000/7c2a990e"
}
```

## Development

To spin up a local development enviroment run: `make dev-run`.

To run tests execute: `make test`
