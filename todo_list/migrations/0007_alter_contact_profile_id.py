# Generated by Django 3.2.6 on 2021-09-11 03:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0006_auto_20210911_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='profile_id',
            field=models.ForeignKey(db_constraint=False, default=1, on_delete=django.db.models.deletion.CASCADE, to='todo_list.profile'),
        ),
    ]
