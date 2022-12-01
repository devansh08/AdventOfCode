#!/bin/fish

set -l year $argv[1]
set -l day $argv[2]
set -l session_cookie $argv[3]

mkdir -p $year
cd $year

mkdir -p Day-$day
cd Day-$day

touch part-1.py part-2.py
curl -LOb "session=$session_cookie" "https://adventofcode.com/$year/day/$day/input"

