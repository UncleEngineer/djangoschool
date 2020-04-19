from django.shortcuts import render, redirect #ดึงมาจาก template
from django.http import HttpResponse #เขียนบนกระดาน
from .models import ExamScore, AllStudent, DocumentUpload
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def HomePage(request):
	#return HttpResponse('<h1>Hello Uncle Engineer</h1>')
	return render(request, 'school/home.html')


def AboutPage(request):
	return render(request, 'school/about.html')


def ContactUs(request):
	return render(request, 'school/contact.html')




def ShowScore(request):
	score = ExamScore.objects.all() #ดึงค่ามาจาก database ทั้งหมด

	context = {'score':score}

	return render(request, 'school/showscore.html', context)




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




#########Search Page###########
# MODELS.objects.all() ดึงค่าทั้งหมด
# MODELS.objects.get(student_id='631001') ดึงค่าแค่ตัวเดียว หากเกินจะ error
# MODELS.objects.filter(level='ม.1') ดึงค่าหลายค่า
#search = AllStudent.objects.get(student_id=)
from django.contrib.auth.decorators import login_required
@login_required
def SearchStudent(request):

	if request.method == 'POST':
		data = request.POST.copy() #
		searchid = data.get('search') #173152
		print(searchid, type(searchid))
		try:
			result = AllStudent.objects.get(student_id=searchid)
			print('RESULT:',result)
			context = {'result':result,'check':'found'}
		except:
			context = {'result':'ไม่มีข้อมูลในระบบ','check':'notfound'}

		return render(request, 'school/search.html',context)

	return render(request, 'school/search.html')



########EDIT PROFILE##########
from django.core.files.storage import FileSystemStorage
from .models import Profile

@login_required
def EditProfile(request):

	username = request.user.username
	current = User.objects.get(username=username)

	if request.method == 'POST' and request.FILES['photo_profile']:
		data = request.POST.copy()
		first_name = data.get('first_name')
		last_name = data.get('last_name')
		email = data.get('email')
		#password = data.get('password')
		
		myprofile = User.objects.get(username=username)
		###file system####
		try:
			setprofile = Profile.objects.get(user=myprofile)
		except:
			setprofile = Profile()
			setprofile.user = myprofile
		file_image = request.FILES['photo_profile']
		file_image_name = request.FILES['photo_profile'].name
		fs = FileSystemStorage()
		filename = fs.save(file_image_name,file_image)
		upload_file_url = fs.url(filename)
		setprofile.photoprofile = upload_file_url[6:]
		setprofile.save()
		#######
		myprofile.username = email
		myprofile.first_name = first_name
		myprofile.last_name = last_name
		myprofile.email = email
		#myprofile.set_password(password)
		myprofile.save()
		# from django.shortcuts import redirect
		return redirect('edit-profile')

	context = {'data':current}
	return render(request, 'school/editprofile.html',context)


def ShowDocument(request):
	document = DocumentUpload.objects.all() #ดึงค่ามาจาก database ทั้งหมด
	context = {'document':document}
	return render(request, 'school/document.html', context)