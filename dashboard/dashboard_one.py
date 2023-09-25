import time

import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(
    page_title="Real-Time Data Science Dashboard",
    page_icon="✅",
    layout="wide",
)

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


# read csv from a github repo
dataset_url = "https://raw.githubusercontent.com/Lexie88rus/bank-marketing-analysis/master/bank.csv"


# read csv from a URL
@st.cache_data
def get_data() -> pd.DataFrame:
    return pd.read_csv(dataset_url)


df = get_data()

# dashboard title
st.title("Real-Time / Live Data Science Dashboard")

# creating a single-element container
placeholder = st.empty()


# near real-time / live feed simulation
for seconds in range(200):
    df["age_new"] = df["age"] * np.random.choice(range(1, 5))
    df["balance_new"] = df["balance"] * np.random.choice(range(1, 5))

    # creating KPIs
    avg_roubletodollar = dollar_course.iloc[-1]

    count_married = brent_price.iloc[-1]

    balance = np.mean(df["balance_new"])

    with placeholder.container():
        # create three columns
        kpi1, kpi2, kpi3 = st.columns(3)

        # fill in those three columns with respective metrics or KPIs
        kpi1.metric(
            label="$ to Rub",
            value=avg_roubletodollar,
            delta=avg_roubletodollar - 96,
        )

        kpi2.metric(
            label="Neft Brent",
            value=count_married,
            delta=-95 + count_married,
        )

        kpi3.metric(
            label="＄ to Barrel",
            value=f"$ {spread_price.iloc[-1] + 95} ",
            delta=2 + spread_price.iloc[-1],
        )

        # create two columns for charts
        fig_col1, fig_col2 = st.columns(2)
        with fig_col1:
            st.markdown("### First Chart")
            fig = px.density_heatmap(
                data_frame=df, y="age_new", x="marital"
            )
            st.write(fig)

        with fig_col2:
            st.markdown("### Second Chart")
            fig2 = px.histogram(data_frame=df, x="age_new")
            st.write(fig2)

        time.sleep(1)