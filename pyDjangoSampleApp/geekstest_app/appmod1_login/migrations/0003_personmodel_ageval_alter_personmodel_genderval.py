# Generated by Django 4.1.7 on 2023-04-15 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appmod1_login', '0002_remove_personmodel_ageval'),
    ]

    operations = [
        migrations.AddField(
            model_name='personmodel',
            name='ageVal',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='personmodel',
            name='genderVal',
            field=models.TextField(choices=[(1, 'male'), (2, 'female'), (3, 'others')], default=1),
        ),
    ]
