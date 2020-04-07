import os
import smtplib

EMAIL_ADDRESS = 'apnamalwa10@gmail.com'
EMAIL_PASSWORD = 'seeyouattop'

with smtplib.SMPT('smtp.gmail.com', 587) as smtp:
	stmp.eclo()
	smtp.starttls()
	stmp.eclo()

	smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

	subject = 'Thanks you contacting Apna Malwa'
	body = 'yes!@'
	msg = f'Subject: {subject}\n\n {body}'

	smpt.sendmail(EMAIL_ADDRESS, 'manishsinghdewas@gmail.com',msg)