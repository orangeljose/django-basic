from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from .models import Project, Task
from .forms import CreateNewProject, CreateNewTask

# Create your views here.

def index(request):
    title = "Django course"
    return render(request, 'index.html', {
        'title': title
    })

def about(request):
    return render(request,'about.html')

def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects/projects.html',{
        'projects' : projects
    })

def tasks(request):
    tasks = Task.objects.all()
    return render(request, "tasks/tasks.html",{
        'tasks' : tasks
    } )

def create_task(request):
    print(request.method)
    if request.method == 'GET':
        return render(request,'tasks/create_task.html',{
            "form" : CreateNewTask
        })
    else:
        Task.objects.create(
        title=request.POST['title'],
        description=request.POST['description'],
        project_id=1)
        return redirect('/tasks')

def create_project(request):
    print(request.method)
    if request.method == 'GET':
        return render(request,'projects/create_project.html',{
            "form" : CreateNewProject
        })
    else:
        Project.objects.create(
        name=request.POST['name'])
        return redirect('/projects')

def project_detail(request, id):
    project = get_object_or_404(Project,id=id)
    tasks = Task.objects.filter(project_id=id)
    return render(request, "projects/detail_project.html",{
        'project' : project,
        'tasks' : tasks
    } )

def task_detail(request, id):
    tasks = get_object_or_404(Task,id=id)
    return render(request, "tasks/detail_task.html",{
        'task' : tasks
    } )
