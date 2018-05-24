# Generated by Django 2.0.4 on 2018-05-14 04:45

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
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Click',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('times', models.PositiveIntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='ClickDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('click', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='details', to='singkat.Click')),
            ],
        ),
        migrations.CreateModel(
            name='Clicker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.GenericIPAddressField(unique=True)),
                ('latitude', models.FloatField(default=0)),
                ('longitude', models.FloatField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='singkat.City')),
            ],
        ),
        migrations.CreateModel(
            name='Continent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='RandomKeywordId',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.BigIntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Singkat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(max_length=100, unique=True)),
                ('target', models.URLField(max_length=2000)),
                ('title', models.CharField(blank=True, max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='singkats', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='clicker',
            name='continent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='singkat.Continent'),
        ),
        migrations.AddField(
            model_name='clicker',
            name='country',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='singkat.Country'),
        ),
        migrations.AddField(
            model_name='click',
            name='ip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='singkat.Clicker'),
        ),
        migrations.AddField(
            model_name='click',
            name='singkat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='singkat.Singkat'),
        ),
    ]
