import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import numpy as np

def run_eda():
    df = pd.read_csv('./data/Car_Purchasing_Data.csv')


    st.text('이 데이터는 Car_Purchasing_Data 데이터 입니다 ')

    radio_menu = ['데이터프레임', '기본통계']
    radio_choice = st.radio('선택하세요', radio_menu)
    if radio_choice == radio_menu[0]:
        st.dataframe(df)
    elif radio_choice == radio_menu[1]:
        st.dataframe(df.describe())

    st.subheader('최대 / 최소값 확인')
    
    min_max_menu = df.columns[4: ]
    select_choice = st.selectbox('컬럼을 선택하세요', min_max_menu)

  

    st.info(f'{select_choice}는 { int(df[select_choice].min())} 부터 {int(df[select_choice].max())} 까지 있습니다. ')

    st.subheader('상관관계분석')

    multi_menu = df.columns[4:]
    st.multiselect('컬럼을 2개 이상 선택하세요', multi_menu)

    # st.dataframe(df.corr(numeric_only=True))

    # fig1 = plt.figure()
    # sb.heatmap(data= df.corr(numeric_only= True), vmin=-1, vmax=1, cmap='coolwarm', annot=True, fmt='.2f', linewidths=0.8)
    # st.pyplot(fig1)
    # 나이대는 20살 부터 70살까지 있다.
    # 연봉은 20000달러부터 100000달러까지 있다.