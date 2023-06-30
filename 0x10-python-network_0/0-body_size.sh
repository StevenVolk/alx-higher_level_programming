#!/bin/bash
# takes a URL, sends a request to that URL and displays the body size
curl -Is "$1" | grep "Content-Length:" | cut -d' ' -f2
