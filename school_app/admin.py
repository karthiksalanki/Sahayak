from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Institute)
class InstituteAdmin(admin.ModelAdmin):
    list_display = ['name','founder_name','principal_name','address','contact_number','email_id','staff_count','students_count']
    
@admin.register(TeacherProfile)
class TeacherProfileAdmin(admin.ModelAdmin):
    list_display = ['name','qualification','department','date_of_birth','contact_number','email_id','address','institute']
    
    
@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ['name','standard','date_of_birth','contact_number','email_id','address','teacher']
    

