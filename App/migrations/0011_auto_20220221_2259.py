# Generated by Django 3.2.12 on 2022-02-21 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0010_auto_20220221_2252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='UUid_Token',
            field=models.UUIDField(default='7313f5b2-e6d9-4d1f-a437-e58423bd8940', editable=False),
        ),
        migrations.AlterField(
            model_name='inventorytest',
            name='Answer1',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='inventorytest',
            name='Answer2',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='inventorytest',
            name='Answer3',
            field=models.CharField(max_length=20),
        ),
    ]
