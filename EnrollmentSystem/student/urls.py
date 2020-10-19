from django.contrib import admin
from django.urls import path
from student import views

app_name = 'student'

urlpatterns = [
    path('', views.home, name='home' ),
    path('add_student/', views.addStudent, name='addStudent' ),
    path('student_details/<int:student_id>/', views.studentDetails, name='studentDetails'),
    path('edit_student/<int:student_id>/', views.editStudent, name='editStudent'),
    path('deleteStudetn/<int:student_id>/', views.deleteStudent, name='deleteStudent')
]

