#!/bin/bash
# Bash script that sends a POST request and displays the body of the response
curl -X POST "$1" -d "email=hr@holbertonschool.com&subject=I will always be here for PLD"
