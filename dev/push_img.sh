#!/usr/bin/env bash

# lower case
github_id=hardysjin

docker tag ci_s1 ghcr.io/$github_id/cmpt756s1:v1
docker tag ci_s2 ghcr.io/$github_id/cmpt756s2:v1
docker tag ci_db ghcr.io/$github_id/cmpt756db:v1

docker push ghcr.io/$github_id/cmpt756s1:v1
docker push ghcr.io/$github_id/cmpt756s2:v1
docker push ghcr.io/$github_id/cmpt756db:v1