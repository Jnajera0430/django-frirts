from django.urls import path
from . import views
urlpatterns = [

    path('signup/', views.signup, name='signUp'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
    path('', views.hola, name='home'),
    path('about/<str:username>', views.about),

    path('project/', views.project, name = 'project'),
    path('create_project/', views.createProject, name = 'createProject'),
    path('detail_project/<int:idProject>', views.projectDetail, name = 'detailProject'),
    path('delete_project/<int:idProject>', views.deleteProject, name = 'deleteProject'),
    path('done_project/<int:idProject>', views.doneProject, name = 'doneProject'),
    path('update_project/<int:idProject>', views.upDateProject, name = 'updateProject'),

    path('listtasks/', views.tasks, name = 'taskList'),
    path('create_task/', views.createTask, name = 'createNewTask'),
    path('tasks/<int:idTask>', views.taskById, name='taskId'),
    path('delete_task/<int:idTask>', views.deleteTask, name='deleteTask'),
    path('done_task/<int:idTask>', views.doneTask, name='doneTask'),
    path('update_task/<int:idTask>', views.updateTask, name='updateTask'),
]