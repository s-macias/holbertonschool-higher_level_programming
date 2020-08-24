#!/bin/bash
# Bash script that takes in a URL, and displays the size of the body of the response
curl -w '%{size_download}\n' -so /dev/null "$1"
