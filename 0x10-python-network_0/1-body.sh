#!/bin/bash
# This Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response
[[ $(curl -s -o /dev/null -w "%{http_code}" "$1") == 200 ]] && curl -s "$1" | sed '$d'
