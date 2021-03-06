# Generated by Django 2.2.12 on 2020-06-02 18:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0002_load_initial_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usersfg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yufgh', models.BigIntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='customtext',
            name='title',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='body',
        ),
        migrations.AddField(
            model_name='customtext',
            name='erfgrtg',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customtext',
            name='fgbhfh',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customtext',
            name='fgs',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customtext',
            name='fgsf',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customtext',
            name='fgsrths',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customtext',
            name='fgvsfhgs',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customtext',
            name='frgrt',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customtext',
            name='gfg',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customtext_gfg', to='home.CustomText'),
        ),
        migrations.AddField(
            model_name='customtext',
            name='hghg',
            field=models.ManyToManyField(blank=True, related_name='customtext_hghg', to='home.CustomText'),
        ),
        migrations.AddField(
            model_name='customtext',
            name='rs',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customtext',
            name='sdawefq',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customtext',
            name='sefewr',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customtext',
            name='trfhtrth',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='hghgh',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='homepage_hghgh', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='homepage',
            name='jhj',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='homepage_jhj', to='home.CustomText'),
        ),
    ]
