# Generated by Django 4.0.3 on 2022-06-11 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_user_birth_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('rates', models.IntegerField()),
                ('text', models.TextField()),
                ('date', models.IntegerField()),
            ],
        ),
    ]
