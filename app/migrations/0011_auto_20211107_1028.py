# Generated by Django 2.2.24 on 2021-11-07 10:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_remove_question_person_que'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='like_ans',
        ),
        migrations.RemoveField(
            model_name='liketoans',
            name='person_anslike',
        ),
        migrations.RemoveField(
            model_name='liketoans',
            name='to_ans',
        ),
        migrations.RemoveField(
            model_name='liketoque',
            name='person_quelike',
        ),
        migrations.RemoveField(
            model_name='liketoque',
            name='to_que',
        ),
        migrations.RemoveField(
            model_name='question',
            name='like_que',
        ),
        migrations.AddField(
            model_name='liketoans',
            name='like_ans',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='like_ans', to='app.Question'),
        ),
        migrations.AddField(
            model_name='liketoque',
            name='like_que',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='like_que', to='app.Question'),
        ),
        migrations.AddField(
            model_name='question',
            name='person_que',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='person_que', to='app.Profile'),
        ),
    ]
