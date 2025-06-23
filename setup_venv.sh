#!/bin/bash

# TODO プロジェクト用の仮想環境セットアップと起動スクリプト

echo "🔧 仮想環境をセットアップ中..."

# プロジェクトディレクトリに移動
cd /Users/natsus/Desktop/todo

# 仮想環境が存在しない場合は作成
if [ ! -d "venv" ]; then
    echo "📦 新しい仮想環境を作成中..."
    python3 -m venv venv
fi

# 仮想環境を有効化
echo "✅ 仮想環境を有効化中..."
source venv/bin/activate

# Pythonとpipのバージョンを表示
echo "🐍 Python バージョン: $(python --version)"
echo "📦 pip バージョン: $(pip --version)"

# pipをアップグレード
echo "⬆️ pipをアップグレード中..."
pip install --upgrade pip

# 現在のディレクトリを表示
echo "📁 現在のディレクトリ: $(pwd)"
echo "✨ 仮想環境が準備完了しました！"
echo ""
echo "💡 以下のコマンドで仮想環境を手動で有効化できます:"
echo "   source venv/bin/activate"
echo ""
