#!/bin/bash
# script to send POST request and displays body
curl -sX POST -d "email: test@gmail.com" -d "subject: I will always be here for PLD" "$1"
