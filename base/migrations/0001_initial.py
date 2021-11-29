# Generated by Django 3.0.3 on 2021-10-17 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tagline', models.TextField()),
                ('headline', models.CharField(max_length=255)),
                ('body_text', models.TextField()),
                ('pub_date', models.DateField(auto_now_add=True)),
                ('mod_date', models.DateField(auto_now=True)),
                ('slug', models.SlugField(max_length=250)),
            ],
        ),
    ]