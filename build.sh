#!/bin/bash

docker build -t python .
docker run -it -v ${PWD}/data/:/data/ python
./git_push_comment.sh
