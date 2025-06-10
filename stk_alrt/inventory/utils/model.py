from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd
from .data_loader import load_data

def train_model(sub_category):
    df = load_data()
    product_df = df[df['Sub-Category'] == sub_category]
    product_df = product_df.groupby('Order Date')['Quantity'].sum().reset_index()
    product_df['Order Date'] = pd.to_datetime(product_df['Order Date'])
    product_df['Days'] = (product_df['Order Date'] - product_df['Order Date'].min()).dt.days
    X = product_df[['Days']]
    y = product_df['Quantity']
    model = LinearRegression().fit(X, y)
    return model, product_df
