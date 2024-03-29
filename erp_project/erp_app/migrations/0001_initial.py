# Generated by Django 5.0.1 on 2024-01-06 12:17

import django.db.models.deletion
import erp_app.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Letter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipient', models.CharField(choices=[('ceo', 'CEO'), ('cto', 'CTO'), ('pm', 'Project Manager')], max_length=50)),
                ('title', models.CharField(default='Title', max_length=40)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('tracking_code', models.IntegerField(default=erp_app.models.generate_tracking_code, unique=True)),
                ('status', models.CharField(choices=[('Sent', 'Sent'), ('Received', 'Received')], default='Sent', max_length=20)),
                ('is_read', models.BooleanField(default=False)),
                ('messages', models.TextField(default='There is no messages.')),
                ('additional_text', models.TextField(blank=True, null=True)),
                ('opened_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='opened_letters', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
