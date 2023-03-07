from django import forms
from .models import Project


class FormsCreateProject(forms.Form):
    name = forms.CharField(label="Nombre del proyecto", max_length=200,
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
    


class FormsCreateTasks(forms.Form):
    
    tarea = forms.CharField(label="Titulo de la tarea", max_length=200)
    descripcion = forms.CharField(
        widget=forms.Textarea, label="Descripcion de la tarea", )
    projects = Project.objects.values_list('id','name', flat= False)
    idProject = forms.ChoiceField(
        choices=projects, label="Selecciona el projecto relacionado")
