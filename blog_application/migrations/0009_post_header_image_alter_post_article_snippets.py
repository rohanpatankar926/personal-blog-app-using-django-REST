# Generated by Django 4.0.6 on 2022-07-31 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_application', '0008_post_article_snippets'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='header_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='article_snippets',
            field=models.CharField(max_length=200),
        ),
    ]
