# Generated by Django 5.1 on 2024-08-09 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_comment_options_alter_post_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='excerpt',
            field=models.TextField(),
        ),
    ]
