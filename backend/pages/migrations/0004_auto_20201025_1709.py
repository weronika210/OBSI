# Generated by Django 3.1.2 on 2020-10-25 16:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20201025_1702'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='room',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='pages.room'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='message',
            name='reservation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pages.reservation'),
        ),
    ]
