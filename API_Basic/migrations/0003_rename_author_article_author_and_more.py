# Generated by Django 4.1.7 on 2023-03-22 07:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('API_Basic', '0002_alter_article_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='Author',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='Date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='Email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='Title',
            new_name='title',
        ),
    ]
