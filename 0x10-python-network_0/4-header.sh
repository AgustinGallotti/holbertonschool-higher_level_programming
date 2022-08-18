#!/bin/bash
# sends a GET request to the URL and dispaly the body repsonse
curl -H "X-HolbertonSchool-User-Id:98" -XGET "$1"
