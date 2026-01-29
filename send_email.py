# import smtplib
# from email.message import EmailMessage
# from datetime import datetime


# EMAIL_ADDRESS = "dxzz23g@gmail.com"
# APP_PASSWORD = " jfae zjwq itsf kadb "
# SUBJECT = "Daily Update"


# def load_emails():
#     with open("emails.txt", "r") as f:
#         return [line.strip() for line in f if line.strip()]
    


# def main():
#     print("Run started:", datetime.now())
#     emails = load_emails()
#     for email in emails:
#         send_email(email)
#         print(f"Sent to {email}")

# def send_email(to_email):
#     msg = EmailMessage()
#     msg["From"] = EMAIL_ADDRESS
#     msg["To"] = to_email
#     msg["Cc"]="rhythmaroraa7@gmail.com"
#     msg["Subject"] = SUBJECT

#     msg.set_content(f"""
# Hello,

# sab active hojaayo

# Regards,
# president aarvak
# """)

#     with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
#         server.login(EMAIL_ADDRESS, APP_PASSWORD)
#         server.send_message(msg)

# def main():
#     emails = load_emails()
#     for email in emails:
#         send_email(email)
#         print(f"Sent to {email}")

# if __name__ == "__main__":
#     main()


from fastapi import FastAPI
from fastapi.responses import JSONResponse
import smtplib
from email.message import EmailMessage

EMAIL_ADDRESS = "dxzz23g@gmail.com"
APP_PASSWORD = "jfae zjwq itsf kadb"
SUBJECT = "Daily Update"

app = FastAPI()

def load_emails():
    with open("emails.txt", "r") as f:
        return [line.strip() for line in f if line.strip()][:20]

def send_email(to_email):
    msg = EmailMessage()
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = to_email
    msg["Subject"] = SUBJECT

    msg.set_content(
        "Hello,\n\n"
        "sab active hojaayo\n\n"
        "Regards,\n"
        "President Aarvak"
    )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL_ADDRESS, APP_PASSWORD)
        server.send_message(msg)

@app.get("/")
def root():
    return {"status": "FastAPI Email Automation running"}

@app.post("/send-mails")
def send_mails():
    emails = load_emails()
    for email in emails:
        send_email(email)
    return JSONResponse(
        content={"status": "success", "sent": len(emails)}
    )
