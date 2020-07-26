# Generated by Django 1.11.2 on 2017-07-10 13:53
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zerver', '0088_remove_referral_and_invites'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='last_active_message_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='long_term_idle',
            field=models.BooleanField(db_index=True, default=False),
        ),
    ]
