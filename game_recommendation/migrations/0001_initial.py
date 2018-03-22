# Generated by Django 2.0.2 on 2018-03-22 17:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('description', models.TextField(null=True)),
                ('year', models.IntegerField(choices=[(2016, 2016), (2000, 2000), (2005, 2005), (2003, 2003), (1997, 1997), (2001, 2001), (1995, 1995), (1990, 1990), (2004, 2004), (1996, 1996), (1991, 1991), (2014, 2015), (2015, 2015), (1998, 1998), (2010, 2010), (2018, 2018), (2009, 2009), (2008, 2008), (2013, 2013), (2011, 2011), (2006, 2006), (1994, 1994), (2012, 2012), (2007, 2007), (1993, 1993), (1992, 1992), (2002, 2002), (2017, 2017)])),
                ('image', models.ImageField(null=True, upload_to='images/')),
                ('top_20', models.NullBooleanField()),
                ('developer', models.ForeignKey(on_delete=None, to='game_recommendation.Developer')),
            ],
        ),
        migrations.CreateModel(
            name='GameScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(blank=True)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game_recommendation.Game')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favorite_developer', models.ForeignKey(blank=True, null=True, on_delete=None, to='game_recommendation.Developer')),
                ('favorite_genre', models.ManyToManyField(blank=True, to='game_recommendation.Genre')),
                ('favorite_tags', models.ManyToManyField(blank=True, to='game_recommendation.Tag')),
                ('user', models.ForeignKey(on_delete=None, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='gamescore',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game_recommendation.User'),
        ),
        migrations.AddField(
            model_name='game',
            name='genre',
            field=models.ManyToManyField(to='game_recommendation.Genre'),
        ),
        migrations.AddField(
            model_name='game',
            name='tags',
            field=models.ManyToManyField(to='game_recommendation.Tag'),
        ),
    ]
