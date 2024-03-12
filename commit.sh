#! /bin/bash

git add .
git commit -m "$1"
git push

git checkout develop
git merge main
git push

git checkout main