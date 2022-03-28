from crud import forms
from django.shortcuts import render

from crud.models import Student

# Create your views here.


def Home(request):
    allstudent = Student.objects.order_by("Fast_Name")
    diction = {"title": "Home", "student": allstudent}
    return render(request, "crud/home.html", context=diction)


def addStudent(request):
    form = forms.StudentFrom()
    if request.method == "POST":
        form = forms.StudentFrom(request.POST)
        if form.is_valid():
            form.save()
            return Home(request)

    diction = {"title": "create from", "form": form}
    return render(request, "crud/addStudent.html", context=diction)


def singalStudent(request, id):
    studentInfo = Student.objects.get(pk=id)
    diction = {"title": "singal student", "studentInfo": studentInfo}
    return render(request, "crud/studentInfo.html", context=diction)


def updateInfo(request, id):
    studentInfo = Student.objects.get(pk=id)
    form = forms.StudentFrom(instance=studentInfo)
    if request.method == "POST":
        form = forms.StudentFrom(request.POST, instance=studentInfo)

        if form.is_valid():
            form.save()
            return Home(request)

    diction = {"title": "update info", "form": form}
    return render(request, "crud/updateInfo.html", context=diction)

def deleteInfo(request,id):
    studentInfo = Student.objects.get(pk=id).delete()
    return Home(request)