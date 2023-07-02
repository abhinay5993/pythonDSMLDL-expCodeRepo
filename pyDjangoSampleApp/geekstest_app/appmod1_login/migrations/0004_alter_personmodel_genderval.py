# Generated by Django 4.1.7 on 2023-04-15 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appmod1_login', '0003_personmodel_ageval_alter_personmodel_genderval'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personmodel',
            name='genderVal',
            field=models.IntegerField(choices=[(1, 'male'), (2, 'female'), (3, 'others')], default=1),
        ),
    ]
