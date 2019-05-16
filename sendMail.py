import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def sendMail(mail):
	f = open("mail_key.txt", "r")
	key=f.read()

	message = Mail(from_email = 'lepowobo@directmail.top',
			to_emails=mail,
			subject='You have a added a new song to the playlist',
			plain_text_content='easy to use',
			html_content='''This is the song you added. 
							Title:
							Artist:
							Lyrics:
							Look for recomendations''')
	try:
		sg=SendGridAPIClient(key)
		response=sg.send(message)
		print(key)

	except Exception as e:
		print(e)