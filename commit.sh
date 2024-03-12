#! /bin/bash

git add .
git commit -m "$1"
git push

get checkout develop
git merge main
git push