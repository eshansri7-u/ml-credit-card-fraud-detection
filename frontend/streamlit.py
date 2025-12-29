import streamlit as st
import requests 

st.set_page_config(
    page_title= "Credit Card Fraud Detection",
    page_icon="💳",
    layout="centered"
)

st.title("Credit Card Fraud Detection")
st.image("image.png")
st.write("A real time credit card fraud detection application powered by a machine learning model and served through a FastAPI backend."
)

st.divider()

st.subheader("Transaction Details")

col1, col2, col3 = st.columns(3)

with col1:
    types = st.slider(
        "Transaction Type",
        min_value=1,
        max_value=5,
        step=1
    )
    
    type_map = {
        1: "Cash In",
        2: "Cash Out",
        3: "Debut",
        4: "Payment",
        5: "Transfer"
    }

    st.caption(f"You selected: {type_map[types]}")

with col2:
    step = st.number_input(
        "Transaction Time (Hour)", min_value=0
        )


with col3:
    amount = st.number_input(
        "Transaction Amount", min_value=0.0
        )

st.divider()

backend_alive = False

try:
    if requests.get("http://localhost:8000/health").status_code == 200:
        backend_alive = True
except:
    pass

if not backend_alive:
    st.warning("Backend if Offline. Start FastAPI first.")
else:
    if st.button("Predict"):
        values = {
            "step": step,
            "types": types,
            "amount": amount
        }

        try:
            response = requests.post("http://localhost:8000/predict", json=values)

            if response.status_code == 200:
                result = response.json()
            
                if result["prediction"] == "fraudulant":
                    st.error("Transaction Is Fraudulant!")
                else:
                    st.success("Transaction is Legitiment")
            else:
                st.error("API Error: Unable to get prediction")
        
        except Exception as e:
            st.error(f"Connection Error {e}")


        






