import smtplib
from fastapi import HTTPException
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from app.settings import APP_SETTINGS

def get_html_content(*, message: str, code) -> str:
    return f"""
        <html>
        <body>
            <p>Hello,</p>
            <p>{message}</p>
            <p>{code}</p>
        </body>
        </htm>
        """


class EmailSender:
    def __init__(self):
        pass
    def get_password_reset_link(self, reset_password_jwt: str):
        app_base_url = APP_SETTINGS.APP_BASE_URL
        return f"{app_base_url}/reset-password-link/{reset_password_jwt}"
    def send_reset_password_email(self, user_email: str, reset_password_jwt: str):
        reset_password_link = self.get_password_reset_link(reset_password_jwt)

        email_html_content = get_html_content(
            message="Click on the link below to reset your password",
            code=reset_password_link
        )
        msg = self.generate_setted_multipart_mime_obj(email_html_content)

        self.try_send_email_message(msg, user_email, response_message="Reset password email sent successfully")


    def send_verification_email(self, user_email: str, otp_code: str):

        # HTML content for the email
        email_html_content = get_html_content(
            message="Bellow is your OTP code to verify your Logly account",
            code=otp_code
        )
        msg = self.generate_setted_multipart_mime_obj(email_html_content)

        self.try_send_email_message(msg, user_email, response_message="Verification email sent successfully")

    def try_send_email_message(self, msg, user_email, response_message: str):
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(APP_SETTINGS.VERIFY_ACCOUNT_SENDER_EMAIL_ADDRESS, APP_SETTINGS.VERIFY_ACCOUNT_SENDER_EMAIL_PASSWORD)
            server.sendmail(APP_SETTINGS.VERIFY_ACCOUNT_SENDER_EMAIL_ADDRESS, user_email, msg.as_string())
            server.quit()
            return {"message": response_message}
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Failed to send email: {str(e)}")
    def generate_setted_multipart_mime_obj(self, email_html_content: str) -> MIMEMultipart:
        msg = MIMEMultipart()
        msg["From"] = APP_SETTINGS.VERIFY_ACCOUNT_SENDER_EMAIL_ADDRESS
        msg["To"] = APP_SETTINGS.VERIFY_ACCOUNT_SENDER_EMAIL_ADDRESS
        msg["Subject"] = "Logly Account Verification"
        msg.attach(MIMEText(email_html_content, "html"))
        return msg