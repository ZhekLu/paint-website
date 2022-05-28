# Generated by Django 4.0.4 on 2022-05-27 19:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('paintsite', '0004_alter_pictureboard_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=30, verbose_name='Author')),
                ('content', models.TextField(verbose_name='Content')),
                ('is_active', models.BooleanField(db_index=True, default=True, verbose_name='Show in the screen?')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Published')),
                ('pp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paintsite.pictureboard', verbose_name='Picture post')),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
                'ordering': ['created_at'],
            },
        ),
    ]