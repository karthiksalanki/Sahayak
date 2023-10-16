from rest_framework import serializers
from .models import *

class InstituteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institute
        fields = '__all__'
        

class TeacherProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherProfile
        fields = '__all__'
        #fields = ['name','qualification','department','date_of_birth','contact_number','email_id','address','institute']
        
class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProfile
        #fields = ['name','standard','date_of_birth','contact_number','email_id','address','teacher']
        fields = '__all__'

  
class StudentProfileSerializer(serializers.ModelSerializer):
    teacher = TeacherProfileSerializer()
    class Meta:
        model = StudentProfile
        fields = ['name','standard','date_of_birth','contact_number','email_id','address','teacher']
        #fields = '__all__'
        
        
        
class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = '__all__'