import streamlit as st
import pickle
import numpy as np

# Load the trained model
model = pickle.load(open('model/xgb_sales_model.pkl', 'rb'))

st.title("📈 Walmart Sales Forecasting App")
st.write("Predict weekly sales for a given store and department using a trained ML model.")

# --- User Inputs ---
store = st.number_input("Store Number", min_value=1, max_value=45, step=1)
dept = st.number_input("Department Number", min_value=1, max_value=100, step=1)
store_type = st.selectbox("Store Type", options=['A', 'B', 'C'])
store_size = st.number_input("Store Size (sqft)", min_value=10000, max_value=250000, step=1000)
is_holiday = st.checkbox("Is Holiday Week?", value=False)

temperature = st.slider("Temperature (°F)", 0.0, 120.0, 75.0)
fuel_price = st.slider("Fuel Price ($)", 2.0, 5.0, 3.0)
cpi = st.slider("CPI", 100.0, 250.0, 180.0)
unemployment = st.slider("Unemployment Rate (%)", 0.0, 15.0, 7.0)

markdown1 = st.slider("MarkDown1", 0.0, 5000.0, 0.0)
markdown2 = st.slider("MarkDown2", 0.0, 5000.0, 0.0)
markdown3 = st.slider("MarkDown3", 0.0, 5000.0, 0.0)
markdown4 = st.slider("MarkDown4", 0.0, 5000.0, 0.0)
markdown5 = st.slider("MarkDown5", 0.0, 5000.0, 0.0)

year = st.selectbox("Year", options=[2010, 2011, 2012])
month = st.slider("Month", 1, 12, 1)
week = st.slider("Week of Year", 1, 52, 1)

lag1 = st.number_input("Sales Last Week (Lag1)", min_value=0.0, max_value=100000.0, value=20000.0)
rolling4 = st.number_input("4-week Rolling Average", min_value=0.0, max_value=100000.0, value=22000.0)

# Encode Store Type
type_encoded = {'A': 0, 'B': 1, 'C': 2}[store_type]

# --- Prediction ---
input_features = np.array([[store, dept, type_encoded, store_size, int(is_holiday),
                            temperature, fuel_price, cpi, unemployment,
                            markdown1, markdown2, markdown3, markdown4, markdown5,
                            year, month, week, lag1, rolling4]])

if st.button("Predict Weekly Sales"):
    prediction = model.predict(input_features)
    st.success(f"📊 Predicted Weekly Sales: ${prediction[0]:,.2f}")
