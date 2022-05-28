# Base Model for the Predict Used Car Prices model for streamlit

import pandas as pd
import numpy as np

def predict_price(hp, cw, es, mpg):
    price = -15824.0382 + 53.610*hp + 4.71*cw + 81.472*es + 36.396*mpg
    return price




