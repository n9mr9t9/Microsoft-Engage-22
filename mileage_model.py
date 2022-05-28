# Base Model for the Predict Mileage model for streamlit

import pandas as pd
import numpy as np

def predict_mpg(cyl, disp, hp, wt, year):
    mpg = -18.026 + 2.36*cyl - (7.64*(10**(-3)))*disp + (2.065*(10**(-4)))*hp - (6.35*(10**(-3)))*wt + (7.97*(10**(-1)))*year
    return mpg

