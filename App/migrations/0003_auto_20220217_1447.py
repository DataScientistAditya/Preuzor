# Generated by Django 3.2.12 on 2022-02-17 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_auto_20220216_2110'),
    ]

    operations = [
        migrations.AddField(
            model_name='wordtest',
            name='TypeofTest',
            field=models.CharField(default='N/A', max_length=20),
        ),
        migrations.AlterField(
            model_name='account',
            name='UUid_Token',
            field=models.UUIDField(default='8e14471d-44f5-45c2-b41b-bf942c918d54', editable=False),
        ),
    ]