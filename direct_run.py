#!/usr/bin/env python3
"""
Flask アプリの直接実行テスト
"""

import sys
import os

# 現在のディレクトリに移動
os.chdir('/Users/natsus/Desktop/todo')

# 仮想環境のPythonパスを追加
venv_path = '/Users/natsus/Desktop/todo/venv/lib/python3.11/site-packages'
if os.path.exists(venv_path):
    sys.path.insert(0, venv_path)

print("🚀 Flask アプリを直接起動中...")
print(f"📁 作業ディレクトリ: {os.getcwd()}")
print(f"🐍 Python パス: {sys.executable}")

try:
    # Flaskをインポート
    from flask import Flask
    print(f"✅ Flask インポート成功")
    
    # app.pyをインポートして実行
    from app import app
    print("✅ app.py インポート成功")
    
    # 環境変数を設定
    os.environ['FLASK_ENV'] = 'development'
    
    print("🌐 Flaskサーバーを起動中...")
    print("📝 ブラウザで http://localhost:5001 にアクセスしてください")
    
    # Flaskアプリを起動
    app.run(debug=True, host='0.0.0.0', port=5001)
    
except Exception as e:
    print(f"❌ エラーが発生しました: {e}")
    import traceback
    traceback.print_exc()
