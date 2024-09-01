import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formatdate

EMAIL_ADDRESS = "ommanivannan@aol.com"
EMAIL_PASSWORD = "rtauheepmjwabhes"  # Replace with your actual password

def send_email():
    try:
        # Set up the server connection
        server = smtplib.SMTP_SSL('smtp.aol.com', 465)  # SSL connection on port 465
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        
        # Construct the email
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = EMAIL_ADDRESS
        msg['Date'] = formatdate(localtime=True)
        msg['Subject'] = "From om test again"
        
        body = "Hello test again."
        msg.attach(MIMEText(body, 'plain'))
        
        # Send the email
        server.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, msg.as_string())
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send email: {e}")


print(f"Sending email to {EMAIL_ADDRESS}... and password is {EMAIL_PASSWORD}")
send_email()
