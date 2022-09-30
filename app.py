import numpy as np
import gzip, pickle, pickletools
import pandas as pd

import streamlit as st

#loading the saved model


filename = "random_forest.pkl"
with gzip.open(filename, 'rb') as f:
    p = pickle.Unpickler(f)
    rf = p.load()


def price_prediction(km_driven, fuel, seller_type, transmission, owner, mileage, engine, max_power, seats, age):
    if fuel == "Diesel":
        fuel = 1
    elif fuel == "Petrol":
        fuel = 4
    elif fuel == "CNG":
        fuel = 0
    elif fuel == "LNG":
        fuel = 2
    elif fuel == "Others":
        fuel = 3

    if owner == "First Owner":
        owner = 0
    elif owner == "Second Owner":
        owner = 2
    elif owner == "Others":
        owner = 1

    if transmission =="Manual":
        transmission = 1
    elif transmission == "Automatic":
        transmission = 0
    elif transmission == "Others":
        transmission = 2

    if seller_type == "Individual":
        seller_type = 1
    elif seller_type == "Dealer":
        seller_type = 0
    elif seller_type == "Others":
        seller_type = 2
    elif seller_type == "Trustmark Dealer":
        seller_type = 3

    prediction = rf.predict(pd.DataFrame([[km_driven, fuel, seller_type, transmission, owner, mileage, engine, max_power, seats, age]]))

    return prediction

def main():
    st.title('Pre-Owned Car Prediction Web App')
    st.markdown("This project was developed by Josiah Adesola")
    st.header("Pre-owned Car in India's Famous Website (Cardekho) ")
    st.subheader("This data was scraped from the Cardekho website, and made available on Kaggle to determine the price of pre-owned vechicles in india. The aim of this project is to help buyers easily predict the price of the price, with their specs in mind.")

    st.image("parked-cars.jpg")

    #get data from user
    km_driven = st.number_input("Kilometer Driven", min_value=1000, max_value=4500000, value=100000)
    fuel = st.selectbox("Fuel Type", ["Diesel", "Petrol", "LPG", "CNG", "Others"])
    age = st.number_input("Age of the car", min_value = 5, max_value=30, value=5)
    mileage = st.number_input("Car's Mileage", min_value=0, max_value=60, value=10)
    engine = st.number_input("Engine Size in CC", min_value=50, max_value=4000, value=1200)
    seller_type = st.selectbox("Seller Type", ["Individual", "Dealer", "Trustmark Dealer", "Others"])
    
    owner = st.selectbox("Level of Pre-ownership", ["First Owner", "Second Owner", "Others"])
    max_power = st.number_input("Maximum Power in BHP", min_value=10, max_value=500, value=100)
    transmission = st.radio("Gear Transmission", ["Manual", "Automatic", "Others"])
    seats = st.number_input("Number of Vehicle's Seat",  min_value=5, max_value=20, value= 5)
    

    #code for prediction
    preciction = 0
    #creating the button for prediction

    if st.button('Predict Price'):
        prediction = price_prediction(km_driven, fuel, seller_type, transmission, owner, mileage, engine, max_power, seats, age)
        prediction = prediction[0]
        prediction =  "This vehicle costs {: ,.2f} Lakhs".format(prediction)
        st.success(prediction)
       

if __name__ == '__main__':
    main()
