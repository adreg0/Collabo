# Generated by Django 3.1.7 on 2021-03-14 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user_tech_stack'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='tech_stack',
            new_name='tech',
        ),
        migrations.RemoveField(
            model_name='user',
            name='bio',
        ),
        migrations.AddField(
            model_name='user',
            name='motives',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Goals and Motives'),
        ),
        migrations.AddField(
            model_name='user',
            name='org_url',
            field=models.URLField(null=True, verbose_name='Organization URL'),
        ),
        migrations.AddField(
            model_name='user',
            name='projects',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Organization Projects'),
        ),
        migrations.AddField(
            model_name='user',
            name='status',
            field=models.CharField(choices=[('1', 'Looking for contributors'), ('2', 'Looking to contribute')], default='1', max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='country',
            field=models.CharField(default='IND', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(default='', max_length=255, verbose_name='First Name/Org Name'),
        ),
    ]
