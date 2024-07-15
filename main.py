import streamlit as st

st.title("weather forecast for the next day")
place = st.text_input("place: ")
days = st.slider("Forecast Days", min_value = 1, max_value = 5,
                  help= "select number of forecast dasy")
option = st.selectbox("Select data to view",
                      ("Temperature", "sky"))
st.subheader(f"{option} for the next {days} days in {place}")
