from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView
from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('',getRecords, name='get-records'),
    path('institute/',createinstitute, name='createInstitue'),
    path('teacher/',createteacher, name='createTeacher'),
    path('student/',createstudent, name='createStudent'),
    
    path("teachers/<int:id>/", getteacher,name='get_teacher'),
    path("students/<int:id>/", getstudent,name='get_student'),
    
    # path('gettoken/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    # path('refreshtoken/',TokenRefreshView.as_view(),name='token_refresh'),
    # path('verifytoken/',TokenRefreshView.as_view(),name='token_verify'),
    path('generate-token/', createcertificate, name='generate_token'),
    path('verify-token/', VerifyToken, name='verify_token'),
    
    
]      