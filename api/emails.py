import smtplib
import getpass

smtp_object = smtplib.SMTP("smtp.gmail.com", 587)
smtp_object.ehlo()

smtp_object.starttls()

email = getpass.getpass("Email: ")
password = getpass.getpass("Password: ")
print(smtp_object.login(email, password))

from_address = "tracy2anucha@gmail.com"
to_address = "tracy2anucha@gmail.com"
subject = input("Enter the Subject Line: ")
message = input("Enter the body message: ")
msg = "Subject: " + subject + "\n" + message

print(smtp_object.sendmail(from_address, to_address, msg))

smtp_object.quit()
