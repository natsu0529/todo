#!/usr/bin/env python3
"""
Streamlit TODO アプリの確実な起動スクリプト
"""

import subprocess
import sys
import os

def main():
    print("🚀 Streamlit TODO アプリを起動中...")
    
    # プロジェクトディレクトリに移動
    os.chdir('/Users/natsus/Desktop/todo')
    print(f"📁 作業ディレクトリ: {os.getcwd()}")
    
    # 仮想環境のPythonを使用
    venv_python = '/Users/natsus/Desktop/todo/venv/bin/python'
    venv_streamlit = '/Users/natsus/Desktop/todo/venv/bin/streamlit'
    
    try:
        # Streamlitがインストールされているか確認
        result = subprocess.run([venv_python, '-c', 'import streamlit; print(f"Streamlit {streamlit.__version__}")'], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ {result.stdout.strip()}")
        else:
            print("❌ Streamlitがインストールされていません")
            print("   仮想環境でpip install streamlitを実行してください")
            return
        
        # Streamlitアプリを起動
        print("🌐 Streamlitサーバーを起動中...")
        print("📝 ブラウザで http://localhost:8501 にアクセスしてください")
        print("⛔ 停止するには Ctrl+C を押してください")
        
        # Streamlitを実行
        subprocess.run([
            venv_streamlit, 'run', 'streamlit_app.py',
            '--server.port', '8501',
            '--server.address', '0.0.0.0',
            '--server.headless', 'false'
        ])
        
    except KeyboardInterrupt:
        print("\n👋 アプリを停止しました")
    except Exception as e:
        print(f"❌ エラーが発生しました: {e}")

if __name__ == "__main__":
    main()
