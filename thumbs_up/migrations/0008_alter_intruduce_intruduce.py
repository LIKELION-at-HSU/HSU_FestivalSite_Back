# Generated by Django 4.2.4 on 2023-10-04 09:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("thumbs_up", "0007_delete_menu"),
    ]

    operations = [
        migrations.AlterField(
            model_name="intruduce",
            name="intruduce",
            field=models.TextField(max_length=2000),
        ),
    ]
