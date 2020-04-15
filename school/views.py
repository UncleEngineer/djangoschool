from django.shortcuts import render, redirect #ดึงมาจาก template
from django.http import HttpResponse #เขียนบนกระดาน

def HomePage(request):
	#return HttpResponse('<h1>Hello Uncle Engineer</h1>')
	return render(request, 'school/home.html')


def AboutPage(request):
	return render(request, 'school/about.html')


def ContactUs(request):
	return render(request, 'school/contact.html')


from .models import ExamScore

def ShowScore(request):
	score = ExamScore.objects.all() #ดึงค่ามาจาก database ทั้งหมด

	context = {'score':score}

	return render(request, 'school/showscore.html', context)


from django.contrib.auth.models import User

def Register(request):

	if request.method == 'POST':
		data = request.POST.copy()
		first_name = data.get('first_name')
		last_name = data.get('last_name')
		email = data.get('email')
		password = data.get('password')
		
		newuser = User()
		newuser.username = email
		newuser.first_name = first_name
		newuser.last_name = last_name
		newuser.email = email
		newuser.set_password(password)
		newuser.save()
		# from django.shortcuts import redirect
		return redirect('home-page')

	return render(request, 'school/register.html')