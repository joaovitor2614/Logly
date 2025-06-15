import smtplib
from fastapi import APIRouter, Request, Response, HTTPException, status
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from app.settings import APP_SETTINGS



class EmailSender:
    def __init__(self):
        pass

    def send_verification_email(self, user_email: str, otp_code: str):

        # HTML content for the email
        email_html_content = f"""
        <html>
        <body>
            <p>Hello,</p>
            <p>Bellow is your OTP code to verify your Logly account</p>
            <p>{otp_code}</p>
        </body>
        </htm>
        """
        msg = MIMEMultipart()
        msg["From"] = APP_SETTINGS.VERIFY_ACCOUNT_SENDER_EMAIL_ADDRESS
        msg["To"] = user_email
        msg["Subject"] = "Email Verification"
        msg.attach(MIMEText(email_html_content, "html"))
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(APP_SETTINGS.VERIFY_ACCOUNT_SENDER_EMAIL_ADDRESS, APP_SETTINGS.VERIFY_ACCOUNT_SENDER_EMAIL_PASSWORD)
            server.sendmail(APP_SETTINGS.VERIFY_ACCOUNT_SENDER_EMAIL_ADDRESS, user_email, msg.as_string())
            server.quit()
            return {"message": "Verification email sent successfully"}
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Failed to send email: {str(e)}")

