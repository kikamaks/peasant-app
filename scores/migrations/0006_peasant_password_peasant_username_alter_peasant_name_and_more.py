# Generated by Django 4.2.1 on 2023-05-31 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("scores", "0005_rename_sirotinja_peasant"),
    ]

    operations = [
        migrations.AddField(
            model_name="peasant",
            name="password",
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AddField(
            model_name="peasant",
            name="username",
            field=models.CharField(blank=True, max_length=256, unique=True),
        ),
        migrations.AlterField(
            model_name="peasant",
            name="name",
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name="peasant",
            name="score",
            field=models.IntegerField(default=0),
        ),
    ]
