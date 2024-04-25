#!/bin/bash
# This Bash script that sends a DELETE request to the URL passed as the first argument and displays the body of the response.
echo $(curl -X DELETE -w "%{http_code}\n" -s -o - "$1")
