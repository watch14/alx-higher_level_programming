#!/bin/bash
# Only status code
curl -sIo /dev/null -w "%{http_code}" "$1"
