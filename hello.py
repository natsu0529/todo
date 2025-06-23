import streamlit as st

st.write("Hello Streamlit!")
st.write("🎉 動作テスト成功！")

if st.button("クリックしてください"):
    st.balloons()
    st.success("ボタンが動作しました！")
