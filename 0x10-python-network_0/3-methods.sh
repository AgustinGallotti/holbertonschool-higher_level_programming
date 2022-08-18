#!/bin/bash
# display all HTTP methods the server wil accept
curl -s -I -X OPTIONS "$1" | grep -i Allow
