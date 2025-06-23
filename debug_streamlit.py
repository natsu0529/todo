import streamlit as st
import sys
import os

st.title("🔍 デバッグ情報")

st.write("## 環境情報")
st.write(f"Python バージョン: {sys.version}")
st.write(f"Streamlit バージョン: {st.__version__}")
st.write(f"現在のディレクトリ: {os.getcwd()}")

st.write("## 環境変数")
for key, value in os.environ.items():
    if 'STREAMLIT' in key or 'PORT' in key or 'PYTHON' in key:
        st.write(f"{key}: {value}")

st.write("## ファイル一覧")
try:
    files = os.listdir('.')
    for file in sorted(files):
        st.write(f"📄 {file}")
except Exception as e:
    st.error(f"ファイル一覧取得エラー: {e}")

st.write("## インポートテスト")
try:
    import json
    st.success("✅ json モジュール OK")
except ImportError as e:
    st.error(f"❌ json モジュール: {e}")

try:
    from datetime import datetime
    st.success("✅ datetime モジュール OK")
    st.write(f"現在時刻: {datetime.now()}")
except ImportError as e:
    st.error(f"❌ datetime モジュール: {e}")

if st.button("メインアプリに戻る"):
    st.switch_page("streamlit_app.py")
