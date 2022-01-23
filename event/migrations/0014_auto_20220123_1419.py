# Generated by Django 2.2.9 on 2022-01-23 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0013_auto_20211209_1131'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='social',
            name='dates',
        ),
        migrations.RemoveField(
            model_name='sports',
            name='dates',
        ),
        migrations.RemoveField(
            model_name='studentwelfare',
            name='dates',
        ),
        migrations.RemoveField(
            model_name='technology',
            name='dates',
        ),
        migrations.AlterField(
            model_name='social',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='social',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='sports',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='sports',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='studentwelfare',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='studentwelfare',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='technology',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='technology',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
