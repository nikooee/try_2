# Generated by Django 2.2.2 on 2019-07-05 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, null=True)),
                ('description', models.CharField(max_length=20, null=True)),
                ('summary', models.TextField(null=True)),
                ('rate', models.FloatField(default=0, null=True)),
                ('like', models.PositiveIntegerField(default=0, null=True)),
                ('release_date', models.DateField(null=True)),
                ('cover', models.ImageField(null=True, upload_to='albums/%Y-%m-%d/')),
            ],
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=20, null=True)),
                ('l_name', models.CharField(max_length=20, null=True)),
                ('nick_name', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, null=True)),
                ('music', models.FileField(upload_to='albums/%Y-%m-%d/')),
            ],
        ),
    ]
