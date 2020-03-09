from django.db import models

# Create your models here.
class College(models.Model):
    College_Name=models.CharField(max_length=200)
    College_id=models.IntegerField()
    Department=models.CharField(max_length=100)

class student(models.Model): 
    college=models.ForeignKey(College,on_delete=models.CASCADE)
    Student_Name=models.CharField(max_length=60)
    Enrollment_no=models.IntegerField(primary_key=True)
    Dob=models.DateTimeField()
    Cgpa=models.IntegerField()
    Address=models.CharField(max_length=100)
    College_Name=models.CharField(max_length=200)
    Branch=models.CharField(max_length=50)

