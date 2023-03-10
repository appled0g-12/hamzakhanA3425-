# Generated by Django 4.1.5 on 2023-02-14 04:20

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
            name='Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='pro/')),
                ('name', models.CharField(max_length=255, null=True)),
                ('town', models.CharField(max_length=255, null=True)),
                ('perfect_in', models.CharField(max_length=255, null=True)),
                ('years_of_experience', models.CharField(max_length=255, null=True)),
                ('availability', models.CharField(max_length=255, null=True)),
                ('pricing', models.CharField(max_length=255, null=True)),
                ('trained_at', models.CharField(max_length=255, null=True)),
                ('additional_text', models.CharField(max_length=500, null=True)),
                ('followers', models.ManyToManyField(blank=True, related_name='following', to=settings.AUTH_USER_MODEL)),
                ('likes', models.ManyToManyField(blank=True, related_name='like', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='card', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='WorkDoneImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workimage', models.ImageField(blank=True, null=True, upload_to='workdonepic/')),
                ('detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workdone', to='artistapp.detail')),
            ],
        ),
    ]
