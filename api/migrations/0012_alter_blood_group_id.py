# Generated by Django 4.2.6 on 2024-02-02 17:15

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_remove_request_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blood_group',
            name='id',
            field=models.CharField(default=uuid.uuid4, editable=False, max_length=36, primary_key=True, serialize=False),
        ),
    ]
