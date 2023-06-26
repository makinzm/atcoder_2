#!/bin/bash

if [[ $# -lt 1 ]]; then
  echo "Error: Insufficient arguments. Usage: $0 <arg1(abcXX)>"
  exit 1
fi

directory="../../$1"

if [ ! -d "$directory" ]; then
  mkdir -p "$directory/src"
  echo "Created directory: $directory"
else
  echo "Directory already exists: $directory"
fi
