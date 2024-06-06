from django.db import models
from django.urls import reverse
from myapp.utils import RUBRICS


class Post(models.Model):
    image = models.ImageField(upload_to='static/image/%Y/%m/%d/', verbose_name='Image')
    title = models.CharField(max_length=50, verbose_name='Title')
    slug = models.SlugField(max_length=50, unique=True, db_index=True, verbose_name="URL")
    article_text = models.TextField(verbose_name='Article text')
    rubric = models.IntegerField(choices=RUBRICS, default=0, verbose_name='Rubric')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Updated')
    publication = models.BooleanField(default=True, verbose_name='Published')

    class Meta:
        db_table = 'post'
        verbose_name = 'article'
        verbose_name_plural = 'Articles'
        ordering = ['id']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})
