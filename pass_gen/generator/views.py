from django.shortcuts import render
from django.http import HttpResponse
import random
import re
import secrets

# Create your views here.
def home(request):
	return render(request, 'generator/home.html')

def password(request):
	thepassword = ''
	characters = list('abcdefghijklmnopqrstuvwxyz')
	if request.GET.get('uppercase'):
		characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
	if request.GET.get('special'):
		characters.extend(list('!"#$%&/?-_,;'))
	if request.GET.get('numbers'):
		characters.extend(list('1234567890'))

	lenght = int(request.GET.get('lenght'))

	for x in range(lenght):
		thepassword += random.choice(characters)

	return render(request, 'generator/password.html', {'password':thepassword})


def generate_pswd():
	thepassword=""
	pattern = re.compile("^[A-Za-z]|[0-9]|[#?!@$%^&*-]")
	for c in range(20):
		thepassword += secrets.choice(pattern)
	print(thepassword)
	return thepassword

