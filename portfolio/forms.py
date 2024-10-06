from django import forms
from .models import Project, Experiencia

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'image', 'url', 'date']

class ExperienciaForm(forms.ModelForm):
    class Meta:
        model = Experiencia
        fields = ['institucion_del_curso', 'descripcion_curso', 'fecha_curso', 'numero_horas']