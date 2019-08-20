#!/bin/bash
#takes in a URL and displays all HTTP methods the server will accept#
curl -s -I "$1" | grep -i "HEAD" | cut -c 8-30
