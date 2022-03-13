#!/usr/bin/env bash

docker cp ../$1/v2/app.py cmpt756$1:/code
docker restart cmpt756$1