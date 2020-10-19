from django.shortcuts import render
from student.models import Students
from student.forms import studentForm

# Create your views here.

def home(request):
    view_student = Students.objects.all()
    return render(request, 'home.html',{'view_student':view_student})

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
    return render(request, 'add_student.html')

def studentDetails(request, student_id):
    student_details = Students.objects.get(id=student_id)
    return render(request, 'student_details.html', {'student_details':student_details})

def editStudent(request, student_id):
    edit_student = Students.objects.get(id=student_id)
    if request.method == 'POST':
        edit_student = Students.objects.get(id=student_id)
        form = studentForm(request.POST, instance=edit_student)
        if form.is_valid():
            form.save()
    return render(request, 'edit_student.html', {'edit_student':edit_student})

def deleteStudent(request, student_id):
    delete_student = Students.objects.get(id=student_id)
    delete_student.delete()
    return home(request)

