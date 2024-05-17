import requests
import pandas as pd

ar = 1    #how many values before the current value does it depend upon
i = 0     #is series stationary or how much to substract from the series to make it stationary
ma = 0    #the moving average or white noise how many values are lagged
r = "r"    # restart control


def callservice(ar, i, ma, days):
    print("Calling forecasting service")
    url = f'http://127.0.0.1:8000/forecast/{ar}/{i}/{ma}/{days}'
    file = {'data_file': open(csvfile, 'rb')}
    resp = requests.post(url=url, files=file) 
    if resp.status_code == 200:
        print("Forecast Was Successful!!!")
        p = input("Enter p to print the forecast values- they are also avalibale in the file called solution.csv\n ")
        if p == 'p':
            print(pd.read_csv("solution.csv"))
        print(f'This forecast was made considering {ar} previous values for each forecast and {i} reduction to make stationry and {ma} previous values in moving average')
    else:
        print("The forecast was not succesfull there is an error in your file or service is not turned on")
        print("make sure to have a 'date' column and name ur column to be forecast 'Units' ")


#(1,0,0) dafault model
while r == 'r':
    print("---:Welcome to the chat bot:---")
    print("--I offer forecasting service for future inventory Using ARIMA model depending on your needs--")
    print("Note: This is a time series forecast and we require the csv to have 2 coulumns: 'Dates' and 'Units' ")
    csvfile = input("To Begin please upload csv file by writing its path: ")
    print("Option 1: Default forcast using 1 previous value and 0 moving average and assuming assuming stationary mean (1,0,0)model")
    print("Option 2: You can customise the AR, I , MA values as you wish:")

    

    opt = input("select which option you want to use for this file:-")

    

    if opt == '1':

        days = input("Select Forecast Horizon days:")
        callservice(1,0,0,days)
        
            
    if opt == '2':
        
        ar = input("Enter auto regression order (int):")
        i =  input("Enter differencing part value (int):")
        ma = input("Enternumber of lagged forecast error terms in the prediction equation:")
        days = input("Enter Forecast Horizon days (int):")
        callservice(ar,i,ma,days)


    print("We have completed the forecast!!!")
    r= input("To restart Enter 'r',  to exit just hit enter:")



