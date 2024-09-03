#!/bin/bash
api_version="2024v1"
url="https://api.staging.floriday.io/suppliers-api-$api_version/swagger/UUID/swagger.json"
target_dir="."
swagger-codegen generate -i $url -l python -o $target_dir