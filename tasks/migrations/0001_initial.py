# Generated by Django 5.0.6 on 2024-06-28 15:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('In Progress', 'In Progress'), ('Completed', 'Completed'), ('Overdue', 'Overdue')], max_length=20)),
                ('priority', models.CharField(choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')], max_length=10)),
                ('due_date', models.DateTimeField()),
                ('category', models.CharField(max_length=255)),
                ('assigned_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
