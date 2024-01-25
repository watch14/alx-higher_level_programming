#!/bin/bash
# cURL only methods
curl -s -X OPTIONS -i "$url" | awk '/Allow:/ {print $2}'
