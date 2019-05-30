import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def sendMail(to,title,message):
	#f = open("mail_key.txt", "r")
	key="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"

	message = Mail(from_email = "laura@planet-travel.club",
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