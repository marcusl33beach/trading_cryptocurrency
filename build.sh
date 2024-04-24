#!/bin/bash

docker build -t python .
docker run -it -v ${PWD}/data/:/data/ python
python3 git_push_comment.py
