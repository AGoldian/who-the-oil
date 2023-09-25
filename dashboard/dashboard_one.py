import pandas as pd
import streamlit as st
import plotly.express as px

st.markdown("<h1 style='text-align: center; background-color: #000045; color: #ece5f6'>U Team</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; background-color: #000045; color: #ece5f6'>3 трек. Кому нефть?</h4>", unsafe_allow_html=True)

st.write("\n")

st.download_button(
        label="Выгрузить новый файл",
        data=r'first_table/Приложение 1.xlsx',
        file_name="new_file.xlsx",  # Укажите желаемое имя файла
        key="download_button",
        )


# Загрузка данных
data = pd.read_excel(r'first_table/Приложение 1.xlsx')
data.columns = data.iloc[0]
data = data.drop(0, axis=0)

# Фильтрация данных
dollar_course = data['Курс $'][data['Курс $'].notna()]
dollar_data = data.iloc[:, 13][data.iloc[:, 13].notna()]
brent_price = data['Цена Brent,\n$/барр.'][data['Цена Brent,\n$/барр.'].notna()]
spread_price = data['Spread (Корректировка),\n$/барр.'][data['Spread (Корректировка),\n$/барр.'].notna()]
freight_price = data['Freight (Корректировка),\n$/барр.'][data['Freight (Корректировка),\n$/барр.'].notna()]

# Заголовок
st.title("NESTRO CHALLENGE")

# График курса доллара
fig_dollar = px.line(x=dollar_data, y=dollar_course, title="Курс доллара, руб.")
st.plotly_chart(fig_dollar)

# График цены на нефть марки Brent
fig_brent = px.line(x=dollar_data[:25], y=brent_price, title="Цена на нефть марки Brent, $")
st.plotly_chart(fig_brent)

# Гистограмма изменения котировок
fig_hist = px.bar(x=dollar_data[:25], y=[brent_price[:25], spread_price[:25], freight_price[:25]],
                  labels={'x': 'Дата', 'y': 'Значение'},
                  title="Гистограмма изменения котировок, $/ барр.",
                  color_discrete_map={'Цена Brent,\n$/барр.': '#E12D39',
                                      'Spread (Корректировка),\n$/барр.': '#17B897',
                                      'Freight (Корректировка),\n$/барр.': '#FFA07A'})
st.plotly_chart(fig_hist)


