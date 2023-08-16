# Generated by Django 4.2.1 on 2023-08-16 04:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("job", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="vacancy",
            name="company",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="job.company",
            ),
        ),
    ]
