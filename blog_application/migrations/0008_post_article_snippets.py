# Generated by Django 4.0.6 on 2022-07-30 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_application', '0007_alter_post_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='article_snippets',
            field=models.CharField(default='Something', max_length=200),
        ),
    ]
