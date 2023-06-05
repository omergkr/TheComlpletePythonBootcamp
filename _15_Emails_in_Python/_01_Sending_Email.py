import smtplib
import getpass

smtp_object = smtplib.SMTP("smtp.gmail.com", 587)
smtp_object.ehlo()
print(smtp_object.starttls())
print("email")
email = "oemergoeker16@gmail.com"
# email = getpass.getpass("enter email please :")
password = "hoofeonqsepfvnvc"
print(smtp_object.login(email, password))
from_address = email
to_address = email
subject = "test"
message = "hallo python"
msg = "Subject: " + subject + "\n" + message

smtp_object.sendmail(from_address, to_address, msg)

