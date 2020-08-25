#!/usr/bin/python3
# Displays the value of the X-Request-Id var. from the header of the response.
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        x_request_id = response.info()['X-Request-Id']
        print(x_request_id)
