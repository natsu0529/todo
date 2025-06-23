#!/bin/bash

# Streamlit開発サーバー起動スクリプト（仮想環境内で実行）

echo "🚀 Streamlit TODO アプリを起動中..."

# プロジェクトディレクトリに移動
cd /Users/natsus/Desktop/todo

# 仮想環境を有効化
source venv/bin/activate

echo "✅ 仮想環境が有効化されました"
echo "🐍 Python: $(which python)"
echo "📦 Streamlit起動中..."

# Streamlitアプリを起動
streamlit run streamlit_app.py
