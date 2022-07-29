# Generated by Django 4.0.6 on 2022-07-28 06:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog_application', '0003_alter_post_title_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='publication_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]