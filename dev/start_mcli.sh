#!/usr/bin/env bash
VER=v0.8

# this is needed to switch M1 Mac to x86 for compatibility with x86 instances/students
ARCH="--platform x86_64"

S2_NAME=cmpt756s2

SERVER=`docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' $S2_NAME`
PORT=30001
echo "LISTEN TO $SERVER"

NETWORK=`docker inspect -f '{{range $key, $value := .NetworkSettings.Networks}}{{$key}} {{end}}' $S2_NAME`

docker run $ARCH -it --rm --network $NETWORK --name mcli mcli:$VER python3 mcli.py $SERVER $PORT
