from fastapi import FastAPI
import smtplib

app = FastAPI()




@app.get("/send/email/{text}")
def send_email(text):
    pass
