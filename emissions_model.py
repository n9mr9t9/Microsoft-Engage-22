# Base Model for the Predict CO2 emissions model for streamlit


import pandas as pd
import numpy as np

def predict_co2(e):
    co2 = 126.289 + 38.992*e
    return co2
