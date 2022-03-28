
from unicodedata import name
from django.urls import include, path

from crud.views import Home, addStudent, deleteInfo, singalStudent, updateInfo

app_name="crud"

urlpatterns = [
    path('',Home,name="home"),
    path('addstudent/',addStudent,name="addStudent"),
    path('studentInfo/<int:id>',singalStudent,name="studentInfo"),
    path('updateInfo/<int:id>',updateInfo,name="updateInfo"),
    path('deleteInfo/<int:id>',deleteInfo,name="deleteInfo"),
]
