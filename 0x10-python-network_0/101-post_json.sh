#!/bin/bash
#Send JSON post request to passed url and display body of response
curl -sX POST $1 -d @$2 -H "Content-Type: application/json"
