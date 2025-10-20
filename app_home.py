import streamlit as st


def run_home():
    st.title("자동차 데이터 분석 및 예측 앱")
    st.info('데이터는 캐글에 있는 Car Price Prediction 데이터를 사용하였습니다.')
    st.text('탐색적 데이터 분석과 자동차 구매 예상 금액 예측 앱입니다.')
    st.image('./image/car.jpg', use_container_width=True)
