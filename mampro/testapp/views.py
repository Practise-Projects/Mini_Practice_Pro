from django.shortcuts import render
from .models import College , student
#from django.http import Http404
#from django.template import loader
# Create your views here.
def student_view(request):
    stu= student.objects.all()
    return render(request,'testapp/student.html',{'stu':stu,})

def college_view(request):
    all_clgs = College.objects.all()
    #template=loader.get_template('testapp/college.html')
    context = {'all_clgs':all_clgs, }

    return render(request,'testapp/college.html',context)
'''
def clg_detail(request,College_id):
    try:
        clg=College.objects.get(pk=College_id)
    except College.DoesNotExist:
        raise Http404("College does not exist")
    return render(request,'testapp/detail.html',{'College':clg})

'''