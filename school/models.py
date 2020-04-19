from django.db import models

class ExamScore(models.Model):

	allsubject = (('คณิตศาสตร์','คณิตศาสตร์'),
				  ('วิทยาศาสตร์','วิทยาศาสตร์'),
				  ('ศิลป','ศิลป'),
				  ('ภาษาอังกฤษ','ภาษาอังกฤษ'),
				  ('ฟิสิกส์','ฟิสิกส์'),
				  ('ชีววิทยา','ชีววิทยา'))

	subject = models.CharField(max_length=200, choices=allsubject, default='คณิตศาสตร์')
	student_name = models.CharField(max_length=200)
	score = models.IntegerField(default=0)

	def __str__(self):
		return self.student_name +'-'+ self.subject +'-' + str(self.score)


class AllStudent(models.Model):
	levellist = ( ('ม.1','ม.1'),
			  ('ม.2','ม.2'),
			  ('ม.3','ม.3'),
			  ('ม.4','ม.4'),
			  ('ม.5','ม.5'),
			  ('ม.6','ม.6'))

	level = models.CharField(max_length=100, choices=levellist, default='ม.1')
	student_name = models.CharField(max_length=200)
	student_id = models.CharField(max_length=200)
	student_tel = models.CharField(max_length=200,blank=True,null=True)
	parent_name = models.CharField(max_length=200,blank=True,null=True)
	parent_tel = models.CharField(max_length=200,blank=True,null=True)
	other = models.TextField(blank=True,null=True)
	photo = models.ImageField(upload_to="studentphoto",blank=True,null=True)

	def __str__(self):
		return '{}-{}'.format(self.student_id,self.student_name)


from django.contrib.auth.models import User

class Profile(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	photoprofile = models.ImageField(default='default.png',upload_to='photo_profile',blank=True,null=True)
	usertype = models.CharField(max_length=100,null=True,blank=True,default='student')

	def __str__(self):
		return f'{self.user.username} Profile'


class DocumentUpload(models.Model):
	levellist = ( ('ม.1','ม.1'),
			  ('ม.2','ม.2'),
			  ('ม.3','ม.3'),
			  ('ม.4','ม.4'),
			  ('ม.5','ม.5'),
			  ('ม.6','ม.6'))

	level = models.CharField(max_length=100, choices=levellist, default='ม.1')
	document_name = models.CharField(max_length=100)
	document = models.FileField(upload_to='alldocument')
	other = models.TextField(blank=True,null=True)
	
	def __str__(self):
		return self.document_name

