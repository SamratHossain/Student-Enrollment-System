from django.shortcuts import render
from student.models import Students
from student.forms import studentForm
from django.contrib import messages

# Create your views here.

def home(request):
    view_student = Students.objects.order_by('id')
    return render(request, 'home.html',{'view_student':view_student, 'title':"Home"})

def addStudent(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        course = request.POST['course']

        student_information = Students(first_name=first_name, last_name=last_name, email=email, phone=phone, address=address, course=course)
        student_information.save()
        messages.success(request, "New Student Added")
    return render(request, 'add_student.html', {'title':"Add Student"})

def studentDetails(request, student_id):
    student_details = Students.objects.get(id=student_id)
    return render(request, 'student_details.html', {'student_details':student_details, 'title':"Student Details"})

def editStudent(request, student_id):
    edit_student = Students.objects.get(id=student_id)
    if request.method == 'POST':
        edit_student = Students.objects.get(id=student_id)
        form = studentForm(request.POST, instance=edit_student)
        if form.is_valid():
            form.save()
            messages.success(request, "Updated Successfully!")
    return render(request, 'edit_student.html', {'edit_student':edit_student, 'title':"Edit Student"})

def deleteStudent(request, student_id):
    delete_student = Students.objects.get(id=student_id)
    delete_student.delete()
    messages.success(request, "Deleted Successfully!")
    return home(request)

def searchStudent(request):
    if request.method == 'GET':
        search = request.GET['search']
        search_student = Students.objects.filter(first_name__icontains=search)
    return render(request, 'search_result.html',{'search_student':search_student})
