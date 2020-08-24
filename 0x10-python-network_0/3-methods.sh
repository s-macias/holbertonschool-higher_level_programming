#!/bin/bash
# Bash script that sends a DELETE request and displays the body of the response
curl -sI "$1" | grep Allow | cut -d ' ' '-f2-'
