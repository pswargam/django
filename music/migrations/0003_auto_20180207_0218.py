# Generated by Django 2.0.1 on 2018-02-07 02:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('music', '0002_album'),
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='music.Album')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RenameModel(
            old_name='Courses',
            new_name='Course',
        ),
        migrations.RenameModel(
            old_name='Students',
            new_name='Student',
        ),
    ]