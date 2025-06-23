#!/usr/bin/env python3
"""
Flask アプリのテスト起動スクリプト
仮想環境の確認とFlaskアプリの実行を行います
"""

import sys
import os
import subprocess

def main():
    print("🔧 Flask アプリテスト起動中...")
    
    # 現在のディレクトリを確認
    current_dir = os.getcwd()
    print(f"📁 現在のディレクトリ: {current_dir}")
    
    # Pythonバージョンを表示
    print(f"🐍 Python バージョン: {sys.version}")
    
    # 仮想環境の確認
    if 'venv' in sys.prefix or 'VIRTUAL_ENV' in os.environ:
        print("✅ 仮想環境が有効化されています")
    else:
        print("⚠️ 仮想環境が有効化されていません")
    
    # Flaskのインポートテスト
    try:
        import flask
        print(f"✅ Flask バージョン: {flask.__version__}")
    except ImportError:
        print("❌ Flaskがインストールされていません")
        print("   pip install flask を実行してください")
        return
    
    # Flask アプリをインポートしてテスト
    try:
        print("🚀 Flask アプリを起動中...")
        from flask_app import app
        
        # テスト環境で起動
        app.run(debug=True, host='0.0.0.0', port=8080)
        
    except Exception as e:
        print(f"❌ エラーが発生しました: {e}")
        print("   flask_app.py を確認してください")

if __name__ == "__main__":
    main()
