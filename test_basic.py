import streamlit as st

# 基本的なテストアプリ
st.title("🧪 Streamlit テストアプリ")
st.write("このページが表示されれば、Streamlitは正常に動作しています！")

st.success("✅ Streamlit正常動作中")

# 簡単なインタラクション
name = st.text_input("あなたの名前を入力してください:")
if name:
    st.write(f"こんにちは、{name}さん！")

# カウンター機能
if 'counter' not in st.session_state:
    st.session_state.counter = 0

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("➕ 増加"):
        st.session_state.counter += 1

with col2:
    st.write(f"カウンター: {st.session_state.counter}")

with col3:
    if st.button("➖ 減少"):
        st.session_state.counter -= 1

st.write("---")
st.info("このテストが成功したら、メインのTODOアプリも動作するはずです！")
