#!/bin/bash
# script to show allowed commands
echo "$(curl -sI "$1")" | grep -i "Allow:" | awk '{for (i=2; i<=NF; i++) printf "%s%s", $i, (i==NF ? "\n" : " ")}'
