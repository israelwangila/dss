# Generated by Django 3.0.7 on 2020-06-26 00:15

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0010_image_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='num_vote_down',
            field=models.PositiveIntegerField(db_index=True, default=0),
        ),
        migrations.AddField(
            model_name='image',
            name='num_vote_up',
            field=models.PositiveIntegerField(db_index=True, default=0),
        ),
        migrations.AddField(
            model_name='image',
            name='vote_score',
            field=models.IntegerField(db_index=True, default=0),
        ),
        migrations.AlterField(
            model_name='comments',
            name='image',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='instagram.Image'),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=cloudinary.models.CloudinaryField(default='image', max_length=255, verbose_name='image'),
        ),
    ]
