#!/bin/bash
# sends a POST request to the passed URL
curl -sd "email=test@gmail.com" -sd "subject=I will always be here for PLD" -XPOST "$1"
