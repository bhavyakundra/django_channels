# Generated by Django 4.1.3 on 2023-01-18 06:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0008_remove_userchatmessages_seen_by_seendetail_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seendetail',
            name='message',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seen_details', to='chat.userchatmessages'),
        ),
    ]
