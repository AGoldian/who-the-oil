import streamlit as st


st.markdown("<h1 style='text-align: center; background-color: #000045; color: #ece5f6'>U Team</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; background-color: #000045; color: #ece5f6'>4 трек. Сколько газа?</h4>", unsafe_allow_html=True)

with st.sidebar:
    st.header("Ввод данных")
    user_input = st.text_area("Введите данные в формате ****")
    uploaded_file = st.file_uploader("Загрузите файл в формате ****")

st.write(user_input)
