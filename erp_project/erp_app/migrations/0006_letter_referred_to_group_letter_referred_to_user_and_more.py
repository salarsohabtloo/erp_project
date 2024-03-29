# Generated by Django 5.0.1 on 2024-01-07 07:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('erp_app', '0005_letter_progress_letterdetails_referred_to_user_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='letter',
            name='referred_to_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='referred_group_letters', to='auth.group'),
        ),
        migrations.AddField(
            model_name='letter',
            name='referred_to_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='referred_letters', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='LetterDetails',
        ),
    ]
