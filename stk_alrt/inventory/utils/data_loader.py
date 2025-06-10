import pandas as pd

def load_data():
    df = pd.read_excel('superstore_sales.xls')
    df = df[df['Category'] == 'Technology']
    df = df.groupby(['Order Date', 'Sub-Category'])['Quantity'].sum().reset_index()
    return df
