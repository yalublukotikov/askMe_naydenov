# Generated by Django 2.2.24 on 2021-11-07 11:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20211107_1028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='person_que',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='person_que', to='app.Profile'),
        ),
    ]
