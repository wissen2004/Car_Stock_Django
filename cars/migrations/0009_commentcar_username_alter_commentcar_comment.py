# Generated by Django 4.1.3 on 2022-12-02 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0008_rename_comment_commentcar'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentcar',
            name='username',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='commentcar',
            name='comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='cars.catal'),
        ),
    ]