# Generated by Django 4.2.16 on 2024-12-05 17:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_post_date_posted_post_published_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='published_date',
            new_name='created_at',
        ),
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
    ]