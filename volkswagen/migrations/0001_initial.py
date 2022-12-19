# Generated by Django 4.1.4 on 2022-12-17 16:52

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='')),
                ('description', models.TextField()),
                ('carType', models.IntegerField(choices=[(0, 'Unknown'), (1, 'Sedan'), (2, 'Hatchback'), (3, 'Universal'), (4, 'SUV'), (5, 'Truck'), (6, 'Minivan'), (7, 'Coupe'), (8, 'Roadster')], default=0)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('user_type', models.IntegerField(choices=[(1, 'ADMIN'), (2, 'VipClient'), (3, 'Client')], default=3, verbose_name='Тип Пользователя')),
                ('phone_number', models.CharField(max_length=50)),
                ('age', models.PositiveIntegerField()),
                ('gender', models.IntegerField(choices=[(1, 'MALE'), (2, 'FEMALE'), (3, 'OTHER')], verbose_name='Гендер')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=60, null=True)),
                ('numbers', models.CharField(max_length=20, null=True)),
                ('mail', models.CharField(max_length=60, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CommentCar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, null=True)),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='volkswagen.catalog')),
            ],
        ),
    ]
