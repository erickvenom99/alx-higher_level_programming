#!/bin/bash
#Extrace the value of content type
curl -s "$1" | wc -c
