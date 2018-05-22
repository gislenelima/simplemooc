from django.db import models

# Create your models here.

class Course(models.Model):
    
    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Atalho')
    description = models.TextField('Descrição', blank = True)
    start_date = models.DateField('Date de Início', null = True, blank = True)
    image = models.ImageField(upload_to='couses/images', verbose_name='Imagem')
    create_at = models.DateTimeField('Criado em',auto_now_add = True)
    update_at = models.DateTimeField('Atualizado em', auto_now = True)

