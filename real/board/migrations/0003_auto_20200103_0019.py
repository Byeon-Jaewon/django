# Generated by Django 3.0.2 on 2020-01-02 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_auto_20200103_0013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='b_date',
            field=models.DateTimeField(),
        ),
    ]
