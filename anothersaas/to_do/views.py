from django.shortcuts import render, redirect
from to_do.models import Todo
from main.models import Status as task_status, Employee as employee

# Create your views here.

def show_index(request):
    data ={
       "todo_status" : task_status.objects.all(),
       "todo_responsible" : employee.objects.all().order_by("id_emp"),
       "todo_list" : Todo.objects.all().order_by('id')
    }
    return render(request,'todo_index.html', data)
    
def add_todo_view(request):
    todo_title = request.POST['todo_title']
    todo_status = task_status.objects.get(status_name = request.POST['status'])
    todo_responsible = employee.objects.get(emp_name = request.POST['responsible'])
    todo_description = request.POST['todo_description']
    Todo.objects.create(title=todo_title,status = todo_status,responsible=todo_responsible, description = todo_description)

    return redirect('to_do')
