# Generated by Django 4.1.7 on 2023-02-19 08:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Muscic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('artist', models.CharField(max_length=120)),
                ('time_length', models.DecimalField(blank=True, decimal_places=2, max_digits=20)),
                ('audio_file', models.FileField(upload_to='musics')),
                ('cover', models.ImageField(upload_to='music_image/')),
                ('album', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='musics.album')),
            ],
        ),
    ]
