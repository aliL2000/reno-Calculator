# Generated by Django 4.2.6 on 2023-10-18 18:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('renoCalc', '0005_homeinspector'),
    ]

    operations = [
        migrations.CreateModel(
            name='Surveyor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('commission', models.JSONField()),
                ('contractor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='renoCalc.contractor')),
            ],
        ),
    ]