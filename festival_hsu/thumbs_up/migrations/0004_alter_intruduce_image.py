# Generated by Django 3.2.20 on 2023-09-23 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thumbs_up', '0003_intruduce_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intruduce',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
