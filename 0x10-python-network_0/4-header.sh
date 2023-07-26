#!/bin/bash
# script for get request with specific header set
curl -sLX GET -H "X-School-User-Id: 98" "$1"
