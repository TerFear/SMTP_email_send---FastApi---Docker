import uvicorn
from fastapi import FastAPI, BackgroundTasks
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from app.mailer import send_mail
from app.config import MailBody

app = FastAPI()




@app.get("/")
def index():
    return {"success" : "Fast Api is worked successful"}



@app.post("/send-email")
def schedule_mail(req: MailBody, tasks: BackgroundTasks):
    data = req.dict()
    tasks.add_task(send_mail, data)
    return {"status": 200, "message": "email has been scheduled"}



if __name__ == "__main__":
    uvicorn.run("main:app", port = 8000 )