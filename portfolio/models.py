from django.db import models
from django.db.models.fields import CharField, DateField, URLField
from django.db.models.fields.files import ImageField
from datetime import date
from django.contrib.auth.models import User 
from django.core.validators import FileExtensionValidator




class Project(models.Model):
    title = CharField(max_length=100)
    description = CharField(max_length=250)
    image = ImageField(
        upload_to="portfolio/images",
        validators=[FileExtensionValidator(['jpg', 'jpeg', 'png'])]  # Valida la extensión del archivo
    )
    url = URLField(blank=True)
    date = DateField(default=date.today)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title

class Experiencia(models.Model):
    institucion_del_curso = models.CharField(max_length=255)
    descripcion_curso = models.TextField()
    fecha_curso = models.DateField()
    numero_horas = models.PositiveIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.institucion_del_curso} - {self.descripcion_curso}"