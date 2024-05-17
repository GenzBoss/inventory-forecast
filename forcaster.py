import pandas as pd
"""
import numpy as np
from statsmodels.tsa.stattools import adfuller
from sklearn.metrics import mean_squared_error
from pmdarima import auto_arima
"""
from statsmodels.tsa.arima.model import ARIMA
import datetime as dt
import warnings
warnings.filterwarnings('ignore')

def forcast_inventory(ar,i, ma, days):
    df = pd.read_csv('Destination.csv')
    df['Date'] = pd.to_datetime(df['Date'] ,format='%Y-%m-%d')
    df=df.set_index('Date')
    train = df[ df.index > (df.tail(1).index[0] -  dt.timedelta(90))]
    y = train['Units']
    #print(y)
    ARIMAmodel = ARIMA(y, order = (ar, i, ma))
    ARIMAmodel = ARIMAmodel.fit()

    future_dates = pd.date_range(start=df.tail(1).index[0] + dt.timedelta(1), end=df.tail(1).index[0] + dt.timedelta(1+days) )
    pred = ARIMAmodel.predict(start = len(df), end = len(df) + days)
    pred.index = future_dates
    #print(pred)
    inventory = pd.DataFrame({'Date':pred.index, 'Inventory forecast':pred.values})
    inventorypivot = pd.pivot_table(inventory, index=['Date'], values=['Inventory forecast'])
    inventorypivot.to_csv('solution.csv')
    #arma_rmse = np.sqrt(mean_squared_error(test["Units"].values, y_pred_df["Predictions"]))
    #print(y_pred_df)
    #print("RMSE: ",arma_rmse)




