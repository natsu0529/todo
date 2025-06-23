#!/usr/bin/env python3
"""
Streamlitアプリの動作テスト
"""

import sys
import os

# プロジェクトディレクトリに移動
os.chdir('/Users/natsus/Desktop/todo')

# 仮想環境のパスを追加
venv_site_packages = '/Users/natsus/Desktop/todo/venv/lib/python3.11/site-packages'
if os.path.exists(venv_site_packages):
    sys.path.insert(0, venv_site_packages)

print("🔍 Streamlitアプリのテスト実行中...")

try:
    # 必要なモジュールをインポート
    import streamlit as st
    print(f"✅ Streamlit {st.__version__} インポート成功")
    
    import json
    print("✅ json モジュール OK")
    
    from datetime import datetime
    print("✅ datetime モジュール OK")
    
    # streamlit_app.pyをインポートしてみる
    print("📝 streamlit_app.py をテスト中...")
    
    # ファイルが存在するか確認
    if os.path.exists('streamlit_app.py'):
        print("✅ streamlit_app.py ファイル存在")
        
        # ファイルの先頭を読み込む
        with open('streamlit_app.py', 'r', encoding='utf-8') as f:
            first_lines = f.readlines()[:10]
        print("📄 ファイル内容（最初の10行）:")
        for i, line in enumerate(first_lines, 1):
            print(f"  {i}: {line.rstrip()}")
            
    else:
        print("❌ streamlit_app.py ファイルが見つかりません")
    
    print("\n🚀 手動でStreamlitを起動するには:")
    print("   cd /Users/natsus/Desktop/todo")
    print("   source venv/bin/activate")
    print("   streamlit run streamlit_app.py")
    
except ImportError as e:
    print(f"❌ インポートエラー: {e}")
    print("   pip install streamlit を実行してください")
except Exception as e:
    print(f"❌ その他のエラー: {e}")

print("\n📋 現在のディレクトリ内容:")
try:
    files = os.listdir('.')
    for file in sorted(files)[:15]:  # 最初の15ファイルのみ表示
        print(f"  📄 {file}")
except Exception as e:
    print(f"❌ ディレクトリ読み込みエラー: {e}")
