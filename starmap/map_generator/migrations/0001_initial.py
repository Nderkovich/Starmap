# Generated by Django 2.2.6 on 2019-10-30 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Starmap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('text', models.TextField(max_length=400)),
                ('city', models.CharField(max_length=250)),
                ('map_type', models.IntegerField(choices=[(1, 'Pdf'), (2, 'Картина')], default=1)),
            ],
        ),
    ]
