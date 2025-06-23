#!/bin/bash

# Flask開発サーバー起動スクリプト（仮想環境内で実行）

echo "🚀 Flask TODO アプリを起動中..."

# プロジェクトディレクトリに移動
cd /Users/natsus/Desktop/todo

# 仮想環境を有効化
source venv/bin/activate

# 環境変数を設定
export FLASK_ENV=development
export FLASK_APP=app.py

echo "✅ 仮想環境が有効化されました"
echo "🐍 Python: $(which python)"
echo "📦 Flask起動中..."

# Flaskアプリを起動
python app.py
