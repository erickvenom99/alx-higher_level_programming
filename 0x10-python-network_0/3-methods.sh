#!/bin/bash
#Displays all HTTP methods
curl -sI "$1" | greP "Allow" | cut -d " " -f 2
