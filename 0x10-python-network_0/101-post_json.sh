#!/bin/bash
# script that sends a JSON POST request
curl -sX POST -H "Content-Type: application/json" --data @"$2" "$1"
