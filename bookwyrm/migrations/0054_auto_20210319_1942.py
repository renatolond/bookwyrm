# Generated by Django 3.1.6 on 2021-03-19 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bookwyrm", "0053_auto_20210319_1913"),
    ]

    operations = [
        migrations.AlterField(
            model_name="importitem",
            name="data",
            field=models.JSONField(),
        ),
        migrations.AlterField(
            model_name="user",
            name="first_name",
            field=models.CharField(
                blank=True, max_length=150, verbose_name="first name"
            ),
        ),
    ]
