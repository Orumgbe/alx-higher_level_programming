#!/bin/bash
#Sends request to url and displays status code
curl -s $1 -w "%{http_code}\n" -o /dev/null
