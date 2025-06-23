import streamlit as st
import sys
import os
import traceback

# 最初にページ設定（必須）
st.set_page_config(
    page_title="デバッグ情報",
    page_icon="🔍",
    layout="wide"
)

st.title("🔍 Streamlit Cloud デバッグ情報")

# セクション1: 基本情報
st.header("1. 基本環境情報")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Python情報")
    st.code(f"バージョン: {sys.version}")
    st.code(f"実行パス: {sys.executable}")

with col2:
    st.subheader("Streamlit情報")
    st.code(f"バージョン: {st.__version__}")

# セクション2: ディレクトリ情報
st.header("2. ディレクトリ情報")
st.code(f"現在のディレクトリ: {os.getcwd()}")

st.subheader("ファイル一覧")
try:
    files = sorted(os.listdir('.'))
    st.write("📁 **ルートディレクトリの内容:**")
    for file in files:
        if os.path.isdir(file):
            st.write(f"📂 {file}/")
        else:
            st.write(f"📄 {file}")
except Exception as e:
    st.error(f"ファイル一覧取得エラー: {e}")

# セクション3: 重要ファイルの存在確認
st.header("3. 重要ファイルの確認")
important_files = ['streamlit_app.py', 'requirements.txt', 'runtime.txt', 'todos.json']

for file in important_files:
    if os.path.exists(file):
        st.success(f"✅ {file} - 存在")
        try:
            with open(file, 'r', encoding='utf-8') as f:
                content = f.read()
            st.code(content[:500] + "..." if len(content) > 500 else content, language='text')
        except Exception as e:
            st.warning(f"⚠️ {file} - 読み込みエラー: {e}")
    else:
        st.error(f"❌ {file} - 存在しない")

# セクション4: インポートテスト
st.header("4. インポートテスト")
test_imports = ['json', 'os', 'datetime']

for module in test_imports:
    try:
        __import__(module)
        st.success(f"✅ {module} - インポート成功")
    except Exception as e:
        st.error(f"❌ {module} - インポートエラー: {e}")

# セクション5: シンプルな機能テスト
st.header("5. 基本機能テスト")

try:
    # フォームテスト
    with st.form("test_form"):
        test_input = st.text_input("テスト入力")
        submit = st.form_submit_button("テスト送信")
        if submit:
            st.success(f"フォーム動作確認: {test_input}")
    
    # カラムテスト
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("テスト1", 10)
    with col2:
        st.metric("テスト2", 20)
    with col3:
        st.metric("テスト3", 30)
    
    st.success("✅ 基本UI要素は正常に動作しています")
    
except Exception as e:
    st.error(f"❌ UI要素エラー: {e}")
    st.code(traceback.format_exc())

# セクション6: 環境変数
st.header("6. 環境変数（抜粋）")
env_vars = ['PYTHONPATH', 'PATH', 'HOME', 'PWD', 'STREAMLIT_SERVER_PORT']
for var in env_vars:
    value = os.environ.get(var, '未設定')
    st.code(f"{var} = {value}")

st.success("🎉 このページが表示されていれば、Streamlitは基本的に動作しています！")
