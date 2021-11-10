# Generated by Django 2.2.24 on 2021-11-06 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20211106_1122'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='like_ans',
        ),
        migrations.AddField(
            model_name='profile',
            name='like_ans',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='like_ans', to='app.LikeToAns'),
        ),
        migrations.RemoveField(
            model_name='profile',
            name='like_que',
        ),
        migrations.AddField(
            model_name='profile',
            name='like_que',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='like_que', to='app.LikeToQue'),
        ),
    ]
