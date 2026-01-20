#!/bin/bash
source ../.env
openapi-generator-cli generate -i http://localhost:${PORT}/api/swagger.yaml -g python -o ../openapi
