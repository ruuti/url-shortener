# URL shortener

## Introduction

"url-shortener" is a URL shortener system that generates a shorter version of a user inputted link.

## Architecture

This system is separated into three different Lambda functions:
* HTTP POST /: accepts POST request with JSON data containing a link to be shortneted
* HTTP GET /{id}: accepts GET request with an id. It returns an object containing a full link to orignial destination.
* Count (not implemented): listens SQS and inserts counts to db

![Architecture](architecture.png?raw=true "System overview")

## Development

To spin up local development enviroment run: `make dev-run`.

To run tests execute: `make test`
