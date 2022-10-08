import smtplib
from email.mime.text import MIMEText


def send_mail(name, branch, rating, comments):
  port = 2525
  smtp_server = 'smtp.mailtrap.io'
  login = 'e3bce6e9c8db03'
  password = 'b0f2ee13f2ac7f'
  message = f"<h3>New Feedback Submission</h3><ul><li>Name: {name}</li><li>Branch: {branch}</li><li>Rating: {rating}</li><li>Comments: {comments}</li></ul>"

  sender_email = 'email1@example.com'
  receiver_email = 'email2@example.com'
  msg = MIMEText(message, 'html')
  msg['Subject'] = 'Dominos Feedback'
  msg['From'] = sender_email
  msg['To'] = receiver_email

# Send email
  with smtplib.SMTP(smtp_server, port) as server:
    server.login(login, password)
    server.sendmail(sender_email, receiver_email, msg.as_string())