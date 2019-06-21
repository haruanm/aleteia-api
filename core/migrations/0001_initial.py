# Generated by Django 2.1.7 on 2019-06-14 21:46

from django.db import migrations, models
import jsonfield.encoder
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClassificationRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='updated_at')),
                ('ipv4', models.CharField(max_length=15, null=True, verbose_name='ipv4')),
                ('ipv6', models.CharField(max_length=40, null=True, verbose_name='ipv6')),
                ('text', models.TextField(verbose_name='text')),
                ('text_date', models.DateTimeField(null=True, verbose_name='text_date')),
                ('url', models.URLField(max_length=2048, verbose_name='url')),
                ('response', jsonfield.fields.JSONField(dump_kwargs={'cls': jsonfield.encoder.JSONEncoder, 'separators': (',', ':')}, load_kwargs={}, verbose_name='response')),
            ],
            options={
                'verbose_name': 'classification request',
                'verbose_name_plural': 'classification requests',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='updated_at')),
                ('date', models.DateTimeField(null=True, verbose_name='date')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('text', models.TextField(verbose_name='text')),
                ('url', models.URLField(max_length=2048, verbose_name='url')),
                ('is_fake', models.BooleanField(null=True, verbose_name='is fake?')),
                ('classified_at', models.DateTimeField(null=True, verbose_name='classified at')),
            ],
            options={
                'verbose_name': 'news',
                'verbose_name_plural': 'news',
            },
        ),
    ]
