#!/bin/bash
#  takes a URL, sends a GET request, and displays the body
curl -sX GET -H "X-School-User-Id: 98" "$1"
