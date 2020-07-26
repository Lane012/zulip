# Generated by Django 1.10.5 on 2017-02-01 22:28
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zerver', '0050_userprofile_avatar_version'),
        ('analytics', '0007_remove_interval'),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name='realmcount',
            index_together={('property', 'end_time')},
        ),
        migrations.AlterIndexTogether(
            name='streamcount',
            index_together={('property', 'realm', 'end_time')},
        ),
        migrations.AlterIndexTogether(
            name='usercount',
            index_together={('property', 'realm', 'end_time')},
        ),
    ]
