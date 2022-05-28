#code for streamlit UI for all three models
#to run in ananconda prompt:   streamlit run apps1.py

import numpy as np
import pandas as pd
from price_model import predict_price
from mileage_model import predict_mpg
from emissions_model import predict_co2
import streamlit as st 
from PIL import Image

def welcome():
    return "Welcome All"

def main():
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Used Car Prices Predictor </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    
    horsepower = st.text_input("Horsepower","Type Here")
    curb_weight = st.text_input("Curb Weight","Type Here")
    engine_size = st.text_input("Engine Size","Type Here")
    highway_mpg = st.text_input("Highway MPG","Type Here")
    result=0
    if st.button("Predict Price"):
        result=float(predict_price(float(horsepower),float(curb_weight), float(engine_size), float(highway_mpg)))
        st.write('The price of car with given specifications is $ {}'.format(result))
    
    
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">CO2 Emissions Predictor </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    enginesize = st.text_input("Engine size","Type Here")
    result1 = 0
    if st.button("Predict CO2 Emissions"):
        result1 = float(predict_co2(float(enginesize)))
        st.write('The CO2 emission emitted are: {}'.format(result1))
        
        
    
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Car Mileage Predictor </h2>
    </div>
    """
    
    st.markdown(html_temp,unsafe_allow_html=True)
    
    cyl = st.text_input("Cylinders: ","Type Here")
    disp = st.text_input("Displacement: ","Type Here")
    hp = st.text_input("Horsepower: ","Type Here")
    wt = st.text_input("Weight: ","Type Here")
    year = st.text_input("Year: ","Type Here")
    result2=0
    if st.button("Predict Mileage"):
        result2=float(predict_mpg(float(cyl),float(disp), float(hp), float(wt), float(year)))
        st.write('The mileage of car with given specifications is {}'.format(result2))

        
if __name__=='__main__':
    main()