#!/bin/bash
#Extrace the value of content type
curl --silent --head $1 | grep -i "Content-Length" | awk '{print $2}'| tr -d '\r'
