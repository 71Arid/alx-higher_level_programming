#!/bin/bash
# Displays the body of a response if the HTTP status code is 200
[ "$(curl -sI "$1" | awk '/^HTTP/ {print $2}')" = 200 ] && curl -s -o - "$1"
