import imaplib
import email

M = imaplib.IMAP4_SSL("imap.gmail.com")
my_email = "oemergoeker16@gmail.com"
password = "hoofeonqsepfvnvc"
print(M.login(my_email, password))
print(M.list())
print(M.select("inbox"))

typ, data = M.search(None, "BEFORE 01-May-2023")
print("typ: " + typ)
typ2, data2 = M.search(None, "FROM user@example.com")
print("typ2: " + typ2)
typ3, data3 = M.search(None, "SUBJECT 'test'")
print("typ3: " + typ)
print(data3)
mail_id = data3[0]
result, email_data = M.fetch(mail_id, "(RFC822)")
print(email_data)
raw_email = email_data[0][1]
raw_string = raw_email.decode("utf-8")

email_message = email.message_from_string(raw_string)
print("**********************")
print(email_message)
print("**********************")
for part in email_message.walk():
    if part.get_content_type() == "text/plain":  # text/html
        body = part.get_payload(decode=True)
        print(body)

