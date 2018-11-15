# Generated by Django 2.1.2 on 2018-10-28 00:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DirFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parentId', models.PositiveIntegerField()),
                ('name', models.CharField(max_length=5000)),
                ('depth', models.PositiveIntegerField()),
                ('pathLineage', models.TextField()),
                ('dorf', models.CharField(choices=[('f', 'file'), ('d', 'directory')], default='m', help_text='File or Directory', max_length=1)),
                ('fileContent', models.TextField()),
                ('modifiedTime', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]