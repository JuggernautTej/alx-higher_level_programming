#!/bin/bash
# This bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
echo $(curl -s -o /dev/null -w '%{size_download}\n' "$1")
