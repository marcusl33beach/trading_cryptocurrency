#!/bin/bash
get add .
current_branch=$(git rev-parse --abbrev-ref HEAD)
changes=$(git diff --cached --name-status)
commit_message=$(echo "$changes" | awk '{ if ($1 == "A") { print "Added: "$2 } else if ($1 == "M") { print "Modified: "$2 } else if ($1 == "D") { print "Deleted: "$2 } }' | awk 'BEGIN{ORS="\n"} {print "- " $0}')
git commit -m "$commit_message"
git push origin "$current_branch"
