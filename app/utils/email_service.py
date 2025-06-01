import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from app.settings import APP_SETTINGS

print('APP_SETTINGS', APP_SETTINGS)

class EmailSender:
    def __init__(self):
        pass

    def send_verification_email(email_data):

        # Create the verification link
        verification_link = f"http://your-website.com"

        # HTML content for the email
        email_html_content = f"""
        <html>
        <body>
            <p>Hello,</p>
            <p>Click the following link to verify your email:</p>
            <a href="{verification_link}">{verification_link}</a>
        </body>
        </htm>
        """
        msg = MIMEMultipart()
        msg["From"] = APP_SETTINGS.VERIFY_ACCOUNT_SENDER_EMAIL_ADDRESS
        msg["To"] = email_data.to_email
        msg["Subject"] = "Email Verification"
        msg.attach(MIMEText(email_html_content, "html"))
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(from_email, password)
            server.sendmail(from_email, email_data.to_email, msg.as_string())
            server.quit()
            return {"message": "Verification email sent successfully"}
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Failed to send email: {str(e)}")

