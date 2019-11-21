# Generated by Django 2.2.7 on 2019-11-21 06:36

import contents.models
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
            name='Gram',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(default='', max_length=128)),
                ('content', models.TextField(default='')),
                ('status', models.CharField(choices=[('1', '초안'), ('2', '발행')], default='1', max_length=5)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '컨텐츠',
                'verbose_name_plural': '컨텐츠',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('resource', models.ImageField(upload_to=contents.models.gen_upload_image_path)),
                ('order', models.SmallIntegerField()),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contents.Gram')),
            ],
            options={
                'verbose_name': '이미지',
                'verbose_name_plural': '이미지',
                'ordering': ['-id'],
                'unique_together': {('content', 'order')},
            },
        ),
    ]
