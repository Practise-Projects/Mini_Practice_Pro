
from django.shortcuts import render
from .models import student
from django.http import Http404

def student (request , stu_id ):

    try:
        stu = student.objects.get(pk=stu_id)
    except student.DoesNotExist:
        raise Http404("Student does not exist")
    return render(request, 'testapp/college.html',  {'stu':stu } )

def college(request):
    all_stu = student.objects.all()
    context = {'all_stu': all_stu }
    return render(request, 'testapp/student.html' ,context )

