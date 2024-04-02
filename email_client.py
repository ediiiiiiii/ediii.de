import smtplib, ssl

port = 587
smtp_server = "smtp.strato.de"
sender = "noreply@ediii.de"
password = "t:K~bML:3h:W5=+"


def send_mail(receiver, subject, message):
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(sender, password)
        server.sendmail(sender, receiver, f"Subject: {subject}\r\n\r\n{message}\r\n".encode("utf-8"))