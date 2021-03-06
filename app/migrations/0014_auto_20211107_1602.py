# Generated by Django 2.2.24 on 2021-11-07 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20211107_1141'),
    ]

    operations = [
        migrations.AddField(
            model_name='liketoans',
            name='person_like_ans',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='person_like_ans', to='app.Profile'),
        ),
        migrations.AddField(
            model_name='liketoque',
            name='person_like_que',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='person_like_que', to='app.Profile'),
        ),
        migrations.AlterField(
            model_name='liketoans',
            name='like_ans',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='like_ans', to='app.Answer'),
        ),
    ]
