#!/bin/bash

filename=$(basename "$1")
# extension="${filename##*.}"
basename="${filename%.*}"

cargo run --bin "$basename"
