# このファイルは Streamlit Cloud でのメインエントリーポイントです
# streamlit_app.py を実行します

import os
import sys

print("🔄 メインアプリ (streamlit_app.py) を読み込んでいます...")

# streamlit_app.py が存在するかチェック
if os.path.exists('streamlit_app.py'):
    # streamlit_app.py の内容を実行
    with open('streamlit_app.py', 'r', encoding='utf-8') as f:
        code = f.read()
    exec(code)
else:
    import streamlit as st
    st.error("streamlit_app.py が見つかりません")
    st.info("このアプリを正常に動作させるには、streamlit_app.py ファイルが必要です。")
