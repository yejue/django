# Generated by Django 2.1 on 2019-12-19 03:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('db_test', '0009_auto_20191217_0115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='c_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='db_test.College'),
        ),
        migrations.AlterField(
            model_name='student',
            name='s_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]