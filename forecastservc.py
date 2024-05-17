from fastapi import FastAPI, File, UploadFile, HTTPException
import uvicorn
import pandas as pd
import shutil
from pydantic import BaseModel
from forcaster import *



def model(ar, i ,ma, days):
	forcast_inventory(ar,i,ma,days)
	
    



app = FastAPI()

#this endpoint is for just example not really useful in project

@app.get("/")
async def root():
    return {"message": "Hello World"}





#this one does all the heavy lifting but needs some error checking to avoid crashing

@app.post('/forecast/{ar}/{i}/{ma}/{days}')
async def forecast(ar, i, ma, days ,data_file: UploadFile = File(...)):
    
    with open("destination.csv", "wb") as buffer:
      shutil.copyfileobj(data_file.file, buffer)
      
	
    model(int(ar), int(i) ,int(ma), int(days))
    
  
      
    return {
        "msg": "we got file succesfully",
        "ar" : ar,
        "i": i,
        "ma" : ma,
        "filename": data_file.filename
        }




if __name__ == '__main__':
	localhost = "127.0.0.1"
	port = 8000
	uvicorn.run(app, host=localhost, port=port)