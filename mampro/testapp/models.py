from django.db import models

# Create your models here.
class College(models.Model):
    College_Name=models.CharField(max_length=200)
    College_id=models.IntegerField(primary_key=True)
    Department=models.CharField(max_length=5)

    def __str__(self):
        a=self.College_Name
        b=str(self.College_id)
        return (a+b)

class student(models.Model): 
    college=models.ForeignKey(College,on_delete=models.CASCADE)
    Student_Name=models.CharField(max_length=60)
    Enrollment_no=models.IntegerField(primary_key=True)
    Dob=models.DateTimeField()
    Cgpa=models.IntegerField()
    Address=models.CharField(max_length=100)
    College_Name=models.CharField(max_length=200)
    Branch=models.CharField(max_length=50)


    def __str__(self):
        a= self.Student_Name
        b=str(self.Enrollment_no)
        return (a+b)
