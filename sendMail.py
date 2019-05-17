import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def sendMail(to,title,message):
	f = open("mail_key.txt", "r")
	key=f.read()

	message = Mail(from_email = "lepowobo@directmail.top",
			to_emails=to,
			subject=title,
			plain_text_content='easy to use',
			html_content=message)
	try:
		sg=SendGridAPIClient(key)
		response=sg.send(message)
		print(key)

	except Exception as e:
		print(e)