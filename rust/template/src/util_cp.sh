#!bin/bash

# Copyするための関数.

if [[ $1 == "help" || $1 == "-h" ]]; then
  echo "$0 <arg1(a.rs)> <arg2(abcXX)>"
  echo "First argument is a code you want copy"
  echo "Second argument is a place you want copy"
  exit 1
fi

if [[ $# -lt 2 ]]; then
  echo "Error: Insufficient arguments. Usage: $0 <arg1(a.rs)> <arg2(abcXX)>"
  echo "If you don't understand how to use it, please use sh $0 -h or sh $0 help."
  exit 1
fi

sh util_init.sh $2

cp $1 ../../$2/src/$1
git add ../../$2/src/$1
git add $1

echo "COPY is done"

git status
