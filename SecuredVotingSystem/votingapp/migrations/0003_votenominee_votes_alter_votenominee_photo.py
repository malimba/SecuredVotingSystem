# Generated by Django 4.1.1 on 2023-06-17 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('votingapp', '0002_alter_votenominee_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='votenominee',
            name='votes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='votenominee',
            name='photo',
            field=models.ImageField(upload_to='static/nomineephotos'),
        ),
    ]
