from .models import Project, Tasks
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from datetime import datetime

now = datetime.now()
# Create your views here.

def signin(request):
    if (request.method == 'GET'):
        return render(request, "signIn.html")
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if (user is None):
            return render(request, "signIn.html", {
                'msg': 'Username or password is incorrect'
            })
        login(request, user)
        return redirect('home')


def signup(request):
    if (request.method == 'GET'):
        return render(request, "signUp.html", {
            'msg': ''
        })
    else:
        if (request.POST['password1'] != request.POST['password2']):
            return render(request, "signUp.html", {
                'msg': "Passwords do not match."
            })

        try:
            user = User.objects.create_user(
                username=request.POST['username'], password=request.POST['password1'])
            user.save()
            login(request, user)
            return redirect('home')
        except:
            return render(request, "signUp.html", {
                'msg': "User already exists."
            })


def signout(request):
    logout(request)
    return redirect('home')


def hola(request):
    titulo = "App Rango"
    return render(request, "index.html", {
        'titulo': titulo
    })


def about(request, username):
    print(username)
    return HttpResponse("Hellow %s" % username)

@login_required
def taskById(request, idTask):
    task = get_object_or_404(Tasks, id=idTask)
    return HttpResponse("task: %s" % task.tarea)

@login_required
def tasks(request):
    tasks = Tasks.objects.filter(user=request.user)
    return render(request, 'tasks/tasks.html', {
        'tasks': tasks, 
    })

@login_required
def createTask(request):
    if (request.method == 'GET'):
        project = Project.objects.filter(user = request.user)
        return render(request, 'tasks/formTask.html', {
            'project': project
        })
    else:
        try:
            Tasks.objects.create(
                tarea=request.POST['tarea'], descripcion=request.POST['descripcion'], project_id=request.POST['project'],
                user=request.user
            )

            return redirect('taskList')
        except ValueError:
            return render(request, 'tasks/formTask.html', {
                'msg': 'Por favor inserta solo datos validos'
            })

@login_required
def deleteTask(request, idTask):
    get_object_or_404(Tasks, id=idTask)
    delTask = Tasks.objects.get(id=idTask)
    delTask.delete()
    return redirect('taskList')

@login_required
def doneTask(request, idTask):
    get_object_or_404(Tasks, id=idTask)
    task = Tasks.objects.values().filter(id=idTask)
    doneTask = Tasks.objects.get(id=idTask)
    if (not task[0]['done']):
        doneTask.dateCompleted = now.date()
    else:
        doneTask.dateCompleted = None
    
    doneTask.done = not task[0]['done']
    doneTask.save()
    return redirect('taskList')
@login_required
def updateTask(request, idTask):
    if(request.method == 'GET'):
        task = get_object_or_404(Tasks, pk = idTask)
        return render(request,"tasks/updatedTask.html",{
            'task': task
        })
    else:
        task = get_object_or_404(Tasks, pk = idTask)
        task.tarea = request.POST['tarea']
        task.descripcion = request.POST['descripcion']
        task.save()
        return redirect('taskList')

@login_required
def createProject(request):
    if (request.method == 'GET'):
        return render(request, "projects/formProject.html")
    else:
        Project.objects.create(name=request.POST['name'], user=request.user)
        return redirect('project')

@login_required
def project(request):
    # projects = list(Project.objects.values())
    projects = Project.objects.filter(user = request.user)
    return render(request, "projects/projects.html", {
        'projects': projects
    })

@login_required
def projectDetail(request, idProject):
    get_object_or_404(Project, id=idProject)
    detailProject = Tasks.objects.all().filter(project=idProject, user = request.user)
    return render(request, 'projects/detailProject.html', {
        'detailProject': detailProject,
        'project': project
    })

@login_required
def deleteProject(request, idProject):
    get_object_or_404(Project, id=idProject)
    delProject = Project.objects.get(id=idProject)
    delProject.delete()
    return redirect('project')

@login_required
def doneProject(request, idProject):
    get_object_or_404(Project, id=idProject)
    project = Project.objects.values().filter(id=idProject)
    doneProject = Project.objects.get(id=idProject)
    if (not project[0]['done']):
        doneProject.dateCompleted = now.date()
    else:
        doneProject.dateCompleted = None
    doneProject.done = not project[0]['done']
    doneProject.save()
    return redirect('project')
@login_required
def upDateProject(request, idProject):
    if(request.method == 'GET'):
        project = get_object_or_404(Project, pk = idProject)
        
        return render(request, "projects/upDateProject.html",{
            'project': project
        })
    else:
        project = get_object_or_404(Project, pk = idProject)
        project.name = request.POST['name']
        project.save()
        return redirect('project')
        
