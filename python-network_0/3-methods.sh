#!/bin/bash
# This Bash script takes in a URL and displays all HTTP methods the server will accept.
curl -i -sL -X OPTIONS "$1" | grep "Allow" | cut -f2 -d":" | tail -c +2
