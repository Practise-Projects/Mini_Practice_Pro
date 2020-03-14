from django.urls import path
from . import views
urlpatterns = [
    path('',views.student_view,name='student_view'),
    path('college/',views.college_view, name='college_view'),
]