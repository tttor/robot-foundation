#!/bin/bash

echo '=== committing ==='
git pull origin master

bash list.sh

git add --all
git commit -a -m fix

echo '=== github.com ==='
git push upstream master
