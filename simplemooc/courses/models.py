from django.db import models

# Create your models here.
class CourseManager (models.Manager):
    #medodo para realizar busca por nome ou slug
    def search(self, query):
        return self.get_queryset().filter(
            models.Q(name__icontains=query) | #ou
            models.Q(description__icontains=query)#models.Q é uma função já inclusa
            
        )


class Course(models.Model):
    
    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Atalho')
    description = models.TextField('Descrição', blank = True)
    start_date = models.DateField('Date de Início', null = True, blank = True)
    image = models.ImageField(upload_to='couses/images', verbose_name='Imagem', null = True, blank = True)
    create_at = models.DateTimeField('Criado em',auto_now_add = True)
    update_at = models.DateTimeField('Atualizado em', auto_now = True)

    objects = CourseManager()
