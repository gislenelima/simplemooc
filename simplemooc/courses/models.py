from django.db import models
from django.urls import reverse
from django.conf import settings

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
    description = models.TextField('Descrição simples', blank = True)
    about = models.TextField('Sobre o curso', blank=True)
    start_date = models.DateField('Date de Início', null = True, blank = True)
    image = models.ImageField(upload_to='media/couses/images', verbose_name='Imagem', null = True, blank = True)
    create_at = models.DateTimeField('Criado em',auto_now_add = True)
    update_at = models.DateTimeField('Atualizado em', auto_now = True)

    objects = CourseManager()

    def __str__(self): # formata os nomes na listagem do admin, deixa bonitinho  admin/course
        return self.name
    
    # @models.permalink
    # def get_absolute_url(self):
    #     return ('details', (), {'slug':self.slug} )
    def get_absolute_url(self):
        return reverse('details', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['name']#ordenar no painel do admin em ordem decrescente



class Enrollment(models.Model):

    STATUS_CHOICES =  {
        (0, 'Pendente'),
        (1, 'Aprovado'),
        (2, 'Cancelado'),
    }
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name = 'Usuário', related_name='enrollments', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, verbose_name = 'Curso', related_name='enrollments', on_delete=models.CASCADE)
    status = models.IntegerField('Situação', choices=STATUS_CHOICES,default=1, blank=True) 
    created_at = models.DateTimeField('Criado em', auto_now_add = True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    def active(self):
        self.status=1
        self.save()

    class Meta:
        verbose_name = 'Inscrição'
        verbose_name_plural = 'Inscrições'
        unique_together = (('user', 'course'),)
    
