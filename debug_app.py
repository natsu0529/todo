import streamlit as st
import os
import sys

st.title("🔍 デバッグ情報")

st.markdown("### 実行環境")
st.write(f"**実行ファイル**: {__file__}")
st.write(f"**作業ディレクトリ**: {os.getcwd()}")
st.write(f"**Python バージョン**: {sys.version}")

st.markdown("### 環境変数")
env_vars = {k: v for k, v in os.environ.items() if 'STREAMLIT' in k or 'PORT' in k}
if env_vars:
    for key, value in env_vars.items():
        st.write(f"**{key}**: {value}")
else:
    st.write("Streamlit関連の環境変数が見つかりません")

st.markdown("### ファイル一覧")
files = [f for f in os.listdir('.') if f.endswith('.py')]
for file in sorted(files):
    st.write(f"- {file}")

st.markdown("---")
st.success("このページが表示されている場合、Streamlitは正常に動作しています。")

# streamlit_app.py の内容を実行
st.markdown("### メインアプリを読み込み中...")

try:
    # streamlit_app.pyの内容を読み込んで実行
    if os.path.exists('streamlit_app.py'):
        with open('streamlit_app.py', 'r', encoding='utf-8') as f:
            app_code = f.read()
        
        # main()関数のみを実行
        st.markdown("---")
        st.markdown("## 📝 TODO アプリ")
        exec(app_code)
    else:
        st.error("streamlit_app.py が見つかりません")
        
except Exception as e:
    st.error(f"エラーが発生しました: {str(e)}")
    st.exception(e)
