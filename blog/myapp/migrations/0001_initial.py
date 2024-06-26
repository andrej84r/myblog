# Generated by Django 5.0.6 on 2024-06-06 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='static/image/%Y/%m/%d/', verbose_name='Image')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('slug', models.SlugField(unique=True, verbose_name='URL')),
                ('article_text', models.TextField(verbose_name='Article text')),
                ('rubric', models.IntegerField(choices=[(1, 'rubric 1'), (2, 'rubric 2'), (3, 'rubric 3'), (4, 'rubric 4'), (5, 'rubric 5'), (6, 'rubric 6')], default=0, verbose_name='Rubric')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('publication', models.BooleanField(default=True, verbose_name='Published')),
            ],
            options={
                'verbose_name': 'article',
                'verbose_name_plural': 'Articles',
                'db_table': 'post',
                'ordering': ['id'],
            },
        ),
    ]
