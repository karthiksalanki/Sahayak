from django.db import models

# Create your models here.

#School or Institute

class Institute(models.Model):
    name = models.CharField(max_length=150)
    founder_name = models.CharField(max_length=150)
    principal_name = models.CharField(max_length=150)
    address = models.TextField()
    contact_number = models.CharField(max_length=225)
    email_id = models.EmailField()
    staff_count = models.PositiveSmallIntegerField(default=0)
    students_count = models.PositiveSmallIntegerField(default=0)
    
    class Meta:
        verbose_name = 'Institute'
        verbose_name_plural = 'Institute' 

    def __str__(self):
        return  self.name
    
class TeacherProfile(models.Model):
    name = models.CharField(max_length=150)
    qualification = models.TextField()
    department = models.CharField(max_length=150)
    date_of_birth = models.DateField(default=None)
    contact_number = models.CharField(max_length=225)
    email_id = models.EmailField()
    address = models.TextField()
    institute = models.ForeignKey(Institute,on_delete=models.DO_NOTHING)
    
    class Meta:
        verbose_name = 'Teachers'
        verbose_name_plural = 'Teachers' 

    def __str__(self):
        return  self.name
    
class StudentProfile(models.Model):
    name = models.CharField(max_length=150)
    standard = models.CharField(max_length=50)
    date_of_birth = models.DateField(default=None)
    contact_number = models.CharField(max_length=225)
    email_id = models.EmailField()
    address = models.TextField()
    teacher = models.ForeignKey(TeacherProfile,on_delete=models.DO_NOTHING)
    institute = models.ForeignKey(Institute,on_delete=models.DO_NOTHING)
    class Meta:
        verbose_name = 'Students'
        verbose_name_plural = 'Students' 

    def __str__(self):
        return  self.name
    
class Certificate(models.Model):
    teacher = models.ForeignKey(TeacherProfile,models.DO_NOTHING)
    student = models.ForeignKey(StudentProfile,models.DO_NOTHING)
    institute = models.ForeignKey(Institute,on_delete=models.DO_NOTHING)
    created_at = models.DateField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Certificates'
        verbose_name_plural = 'Certificates' 


