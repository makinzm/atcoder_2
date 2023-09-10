#!/bin/bash

# コンテスト中にRunするための関数 (utilコマンドはつけない.)

filename=$(basename "$1")
# extension="${filename##*.}"
basename="${filename%.*}"

cargo run --bin "$basename"
