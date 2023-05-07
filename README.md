# python-web-bottle-basic-auth-api-raw-cockroachdb-multi-node-without-ssl-simple

## Description
Simple web app that serves an api
for a bottle project.

Uses sqlalchemy with raw sql to query a table `dog`.

Requires basic authentication for CRUD opperations.

| username | password |
| -------- | -------- |
| *user* | *pass* |

Remotely tested with *testify*.

## Tech stack
- python
  - bottle
  - sqlalchemy
  - testify
  - requests
- cockroachdb

## Docker stack
- python:latest
- cockroachdb/cockroach:v19.2.4

## To run
`sudo ./install.sh -u`
- Get all dogs: http://localhost/dog
  - Schema id, breed, and color
- CRUD opperations
  - Create: curl -i -X PUT localhost/dog/<id> -u 'user:pass'
  - Read: http://localhost/dog/<id> -u 'user:pass'
  - Update: curl -i -X POST localhost/dog/<id>/<breed>/<color> -u 'user:pass'
  - Delete: curl -i -X DELETE localhost/dog/<id> -u 'user:pass'

## To stop
`sudo ./install.sh -d`

## For help
`sudo ./install.sh -h`