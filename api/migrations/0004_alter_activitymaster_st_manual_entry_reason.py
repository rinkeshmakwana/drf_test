# Generated by Django 3.2.7 on 2021-09-29 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_activity_in_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activitymaster',
            name='st_manual_entry_reason',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
