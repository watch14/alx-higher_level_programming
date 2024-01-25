#!/bin/bash
# curl a json file
curl -s -X POST -H "Content-Type: application/json" --data-binary "@$filename" "$url"
