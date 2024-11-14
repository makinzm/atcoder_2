#!/bin/bash

# requirements.txt が存在するかチェック
if [[ ! -f requirements.txt ]]; then
  echo "Error: requirements.txt が見つかりません。"
  exit 1
fi

echo "パッケージをインストールしています..."

# requirements.txt から各パッケージを読み込んでインストール
while read -r package; do
  if [[ -n "$package" && ! "$package" =~ ^# ]]; then
    echo "Installing $package..."
    uv add "$package" || {
      echo "Error: $package のインストールに失敗しました。"
      exit 1
    }
  fi
done < requirements.txt

uv add pip
uv sync

uv run pip3 install git+https://github.com/not522/ac-library-python

echo "全てのパッケージが正常にインストールされました。"

