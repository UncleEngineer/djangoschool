from django.contrib import admin
from .models import ExamScore, AllStudent, Profile, DocumentUpload

# Register your models here.

admin.site.register(ExamScore)

class StudentAdmin(admin.ModelAdmin):
	list_display = ['student_id','level','student_name','student_tel']
	list_filter = ['level']
	list_editable = ['student_tel']


admin.site.register(AllStudent, StudentAdmin)
admin.site.register(Profile)
admin.site.register(DocumentUpload)