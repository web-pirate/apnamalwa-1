from django.shortcuts import render, redirect
from django.http import HttpResponse 
from .models import user_data
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from smtplib import SMTP

def index(request):
	if request.method=="POST":
		try:
			print('Form is Submitted Successfully!!')
			name = request.POST.get("name")
			print(name)
			email = request.POST.get("email")
			phone = request.POST.get("phone")
			city = request.POST.get("city")
			
			message = request.POST.get("message")

			print(email, phone)

			
			

			form_info = user_data(name=name,email=email,phone=phone,city=city,message=message)

			form_info.save()
			messages.success(request, f'{name} your form is succesfully sent.')
			print('fromsave')
			
			try:
				send_mail(
				f'One New Entry of {name}',
				'Here is the message.',
				settings.EMAIL_HOST_USER,
				['vishalsinghdewas2@gmail.com'],
				print('mail btw'),
				fail_silently=False,
				)

			except:
				print('Email is not valid')


			return redirect(index)
			print('almost done')

		except:
			pass

	else:
		return render(request, 'user/index.html')
			
