#!/bin/bash
# Get the comtent length of a giving ip address
curl -sI "$1" | awk '/Content-Length/{print $2}'
