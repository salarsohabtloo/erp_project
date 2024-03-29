# Generated by Django 5.0.1 on 2024-01-07 06:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('erp_app', '0002_letter_referred_to'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='letter',
            name='referred_to',
        ),
        migrations.CreateModel(
            name='LetterDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('additional_text', models.TextField(blank=True, null=True)),
                ('letter', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='erp_app.letter')),
                ('referred_to_group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='auth.group')),
            ],
        ),
    ]
