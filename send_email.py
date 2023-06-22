import smtplib
from email.message import EmailMessage

def send_email(name, email, topic):
    # Email content
    subject = "Registration"
    message = f"Name: {name}\nEmail: {email}\nTopic: {topic}"

    # Sender and recipient details
    sender = "hackshark51@gmail.com"
    recipient = "aayushiagarwal4094@gmail.com"

    # Create EmailMessage object
    email_msg = EmailMessage()
    email_msg.set_content(message)
    email_msg["Subject"] = subject
    email_msg["From"] = sender
    email_msg["To"] = recipient

    # Send the email
    try:
        smtp_server = "smtp.elasticemail.com"  # Update with your SMTP server details
        smtp_port = 587  # Update with your SMTP server port
        smtp_username = "hackshark51@gmail.com"  # Update with your SMTP username
        smtp_password = "1D53CC2BE57619E3301F491D84DBC9DDDB88"  # Update with your SMTP password

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.send_message(email_msg)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    topic = input("Enter your topic: ")
    send_email(name, email, topic)
