#!/bin/bash
# request the content lenght in bytes
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
