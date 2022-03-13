#!/usr/bin/env bash
docker-compose down

docker rmi --force ci_db:latest ci_s1:latest ci_s2:latest ci_test:latest

docker-compose build --no-cache
docker-compose up