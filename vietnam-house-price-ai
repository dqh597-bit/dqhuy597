import streamlit as st
import pandas as pd
import joblib

model = joblib.load("models/model.pkl")
scaler = joblib.load("models/scaler.pkl")
features = joblib.load("models/features.pkl")

st.set_page_config(
    page_title="AI Dự Đoán Giá Nhà Việt Nam",
    page_icon="🏠",
    layout="wide"
)

st.title("🏠 HỆ THỐNG AI DỰ ĐOÁN GIÁ NHÀ VIỆT NAM")

st.write("Ứng dụng Machine Learning dự đoán giá bất động sản Việt Nam")

st.sidebar.header("Nhập thông tin nhà")

dien_tich = st.sidebar.number_input("Diện tích (m²)", 20, 500, 80)
phong_ngu = st.sidebar.number_input("Số phòng ngủ", 1, 10, 3)
phong_tam = st.sidebar.number_input("Số phòng tắm", 1, 10, 2)
so_tang = st.sidebar.number_input("Số tầng", 1, 15, 3)

quan = st.sidebar.selectbox(
    "Quận/Huyện",
    [
        "Cầu Giấy",
        "Ba Đình",
        "Đống Đa",
        "Thanh Xuân",
        "Hà Đông",
        "Nam Từ Liêm",
        "Hoàng Mai",
        "Long Biên"
    ]
)

input_dict = {
    "dien_tich": dien_tich,
    "phong_ngu": phong_ngu,
    "phong_tam": phong_tam,
    "so_tang": so_tang
}

for feature in features:
    if feature.startswith("quan_"):
        input_dict[feature] = 0

quan_col = f"quan_{quan}"

if quan_col in features:
    input_dict[quan_col] = 1

input_df = pd.DataFrame([input_dict])

input_df = input_df.reindex(columns=features, fill_value=0)

st.subheader("Thông tin đã nhập")
st.write(input_df)

input_scaled = scaler.transform(input_df)

if st.button("Dự đoán giá nhà"):
    prediction = model.predict(input_scaled)[0]

    st.success(
        f"Giá nhà dự đoán: {prediction:,.0f} triệu VNĐ"
    )

st.markdown("---")

st.header("Thông tin dự án")

st.write("""
✔ Dataset nhà Việt Nam

✔ Data preprocessing

✔ Train/Test split

✔ XGBoost Machine Learning

✔ Streamlit Web App

✔ Realtime prediction

✔ Visualization và EDA
""")
