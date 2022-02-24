# Generated by Django 3.2.12 on 2022-02-21 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0008_auto_20220220_1702'),
    ]

    operations = [
        migrations.CreateModel(
            name='InventoryTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Question', models.CharField(max_length=500)),
                ('Answer1', models.CharField(choices=[('Always', 'Always'), ('Sometime', 'Sometime'), ('Never', 'Never')], max_length=20)),
                ('Answer2', models.CharField(choices=[('Always', 'Always'), ('Sometime', 'Sometime'), ('Never', 'Never')], max_length=20)),
                ('Answer3', models.CharField(choices=[('Always', 'Always'), ('Sometime', 'Sometime'), ('Never', 'Never')], max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='is_IntelligenceTest',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='account',
            name='is_InventoryTest',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='account',
            name='is_PostTest',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='account',
            name='UUid_Token',
            field=models.UUIDField(default='fd122257-6e48-4044-9c75-2d8ae5c62ca9', editable=False),
        ),
    ]