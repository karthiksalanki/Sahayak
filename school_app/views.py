from django.shortcuts import render
from school_app.serializers import *
from rest_framework import status,permissions,authentication
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
import json
from rest_framework.views import APIView
import jwt
from django.conf import settings
# Create your views here.


# create institute data 
@api_view(['POST'])
def createinstitute(request):
    try:
        # data={
        #     'name':request.data['name'],
        #     'founder_name':request.data['founder_name'],
        #     'principal_name':request.data['principal_name'],
        #     'email_id':request.data['email_id'],
        #     'address':request.data['address'],
        #     'contact_number':request.data['contact_number'],
        # }
        # institutedata = Institute.objects.create(**data)
        # institutedata.save()
        serializer = InstituteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Institute':serializer.data},status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)
    except Exception as e:
        return Response(str(e))

# create teacher data 
@api_view(['POST'])
def createteacher(request):
    try:
        instituedata = Institute.objects.get(name = request.data['institute'])
        data={
            'name':request.data['name'],
            'qualification':request.data['qualification'],
            'department':request.data['department'],
            'date_of_birth':request.data['date_of_birth'],
            'contact_number':request.data['contact_number'],
            'email_id':request.data['email_id'],
            'address':request.data['address'],
            'institute_id':instituedata.id,
        }
        teacherdata = TeacherProfile.objects.create(**data)
        teacherdata.save()
        serializer = TeacherProfileSerializer(teacherdata)
        return Response({'Teacher':serializer.data},status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response(str(e))


# create student data 
@api_view(['POST'])
def createstudent(request):
    try:
        institutedata = Institute.objects.get(name = request.data['institute_id'])
        teacherdata = TeacherProfile.objects.get(name = request.data['teacher_id'])
        data={
            'name':request.data['name'],
            'standard':request.data['standard'],
            'date_of_birth':request.data['date_of_birth'],
            'contact_number':request.data['contact_number'],
            'email_id':request.data['email_id'],
            'address':request.data['address'],
            'teacher_id':teacherdata.id,
            'institute_id':institutedata.id,
        }
        studentdata = StudentProfile.objects.create(**data)
        studentdata.save()
        serializer = StudentsSerializer(studentdata)
        # serializer = StudentsSerializer(data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response({'Institute':serializer.data},status=status.HTTP_201_CREATED)
        return Response({'Student':serializer.data},status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response(str(e))

#base or all records
@api_view(['GET'])
def getRecords(request):
    # try:
        institute = Institute.objects.all()
        teachers = TeacherProfile.objects.all()
        students = StudentProfile.objects.all()
        print(teachers,students,institute)
        teacher_serializer = TeacherProfileSerializer(teachers)
        student_serializer = StudentsSerializer(students)
        institute_serializer = InstituteSerializer(institute)
        return Response({'Institute_List':institute_serializer.data,'Teachers List':teacher_serializer.data,'Students List':student_serializer.data})
    # except Exception as e:
    #     return Response(str(e))

#To get teacher and associated students
@api_view(['GET'])
def getteacher(request,id):
    try:
        if request.method == 'GET':
            teacherdata = TeacherProfile.objects.get(id = id)
            students = StudentProfile.objects.filter(teacher_id=id )                      #teacherdata.teacher_name.all()
            serializer = StudentsSerializer(students, many=True)
            return Response({'teacher':teacherdata.name,'assigned-students':serializer.data},status=status.HTTP_200_OK)
    except Exception as e:
        return Response(str(e))

#To get student and associated teacher
@api_view(['GET'])
def getstudent(request,id):
    try:
        if request.method == 'GET':
            studentdata = StudentProfile.objects.get(id=id)
            serializer = StudentProfileSerializer(studentdata)
            return Response({'student':serializer.data},status=status.HTTP_200_OK)
    except Exception as e:
        return Response(str(e))
    
#choosing teacher and student pair OR  Generating certificate
@api_view(['POST'])
def createcertificate(request):
    try:
        if request.method == 'POST':
            teacher = request.data['teacher']
            student = request.data['student']
            teacherdata = TeacherProfile.objects.get(name=teacher)
            studentdata = StudentProfile.objects.get(name=student)
            print(teacherdata,studentdata)
            if studentdata.teacher_id == teacherdata.id:
                certificate_data = Certificate.objects.create(teacher=teacherdata,student=studentdata,institute=studentdata.institute)
                certificate_data.save()
                serializer = CertificateSerializer(certificate_data)
                payload = {
                    'teacher': teacher,
                    'student': student,
                }
                token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
                return Response({'token': token,'certificate':serializer.data})
            else:
                return Response({'msg':f'Not Allowed.({student} is not assigned to {teacher})'})
    except Exception as e:
        return Response(str(e))
        #eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0ZWFjaGVyIjoiU29tYXNoZWtoYXIgayIsInN0dWRlbnQiOiJrYXJ0aGlrIGtzIn0.njpFrVtzTzCa9FdhNzLntmG1m8F6gLQc65HFlet_jy0
        
# verify token        
@api_view(['POST'])
def VerifyToken(request):
    try:
        token = request.data.get('token')
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            return Response({'payload': payload,'msg':"verified with token"})
        except jwt.ExpiredSignatureError:
            return Response({'error': 'Token has expired.'})
        except jwt.InvalidTokenError:
            return Response({'error': 'Invalid token.'})
    except Exception as e:
        return Response(str(e))
    
