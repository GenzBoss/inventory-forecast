This is a chatbot service that predicts future inventory using time value analysis:
This repository contains 3 python files:
chatbot.py
forecastservic.py
forecaster.py

The application uses ARIMA model to initial time value forecast

In order to use this appplication we need 2 terminal or processes , first is this forecastservic.py which will create a server with api endpoints to host forecast service and second is the chatbot that will interact with the endpoint to call the service based on user input.

I have created a test.csv file to take tests, the csv file is required to have a column named 'date' and a column named 'Units' which will be used for training the model for forecast

There is still some need to handle exceptions properly but otherwise the application should be working correctly. 



sample output:
![image](https://github.com/GenzBoss/inventory-forecast/assets/99097730/7fb45a05-be7a-41c1-b2c2-7b443148207c)

