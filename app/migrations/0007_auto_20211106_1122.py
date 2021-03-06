# Generated by Django 2.2.24 on 2021-11-06 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_remove_question_answer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='like_ans',
        ),
        migrations.RemoveField(
            model_name='question',
            name='like_que',
        ),
        migrations.AddField(
            model_name='profile',
            name='like_ans',
            field=models.ManyToManyField(related_name='like_ans', to='app.LikeToAns'),
        ),
        migrations.AddField(
            model_name='profile',
            name='like_que',
            field=models.ManyToManyField(related_name='like_que', to='app.LikeToQue'),
        ),
    ]
