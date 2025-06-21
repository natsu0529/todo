import streamlit as st

# このファイルは Streamlit Cloud でのメインエントリーポイントです
# 実際のアプリは streamlit_app.py にあります

st.title("🔄 リダイレクト中...")
st.info("このページは自動的にメインアプリにリダイレクトされます。")

# JavaScript を使用してリダイレクト
st.markdown("""
<script>
window.location.href = 'streamlit_app.py';
</script>
""", unsafe_allow_html=True)

# Python でのリダイレクト
st.markdown("メインアプリを読み込んでいます...")

# streamlit_app.py の内容を実行
exec(open('streamlit_app.py').read())
