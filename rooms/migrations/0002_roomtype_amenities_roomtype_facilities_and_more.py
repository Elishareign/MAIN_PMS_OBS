# Generated by Django 5.0.10 on 2024-12-15 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='roomtype',
            name='amenities',
            field=models.TextField(default='{}'),
        ),
        migrations.AddField(
            model_name='roomtype',
            name='facilities',
            field=models.TextField(default='{}'),
        ),
        migrations.AlterField(
            model_name='roomtype',
            name='room_description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='roomtype',
            name='room_size',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='roomtype',
            name='room_type_name',
            field=models.CharField(max_length=100),
        ),
    ]