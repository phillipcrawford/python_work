# Generated by Django 5.1.4 on 2024-12-12 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0003_entry'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='text',
            field=models.TextField(default='hmm'),
            preserve_default=False,
        ),
    ]
