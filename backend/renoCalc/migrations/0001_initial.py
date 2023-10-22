# Generated by Django 4.2.6 on 2023-10-22 17:51

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('phoneNumber', models.CharField(blank=True, max_length=15, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='ContractorModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phoneNumber', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=100)),
                ('website_link', models.URLField(blank=True, null=True)),
                ('rating', models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PropertyTypeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='RegionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UserHomeAndRenovationConfigurationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uniqueConfiguration', models.JSONField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SurveyorModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('commission', models.JSONField()),
                ('contractor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='renoCalc.contractormodel')),
            ],
        ),
        migrations.CreateModel(
            name='RealEstateLaywerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('commission', models.JSONField()),
                ('contractor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='renoCalc.contractormodel')),
            ],
        ),
        migrations.CreateModel(
            name='RealEstateAgentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('commission', models.JSONField()),
                ('contractor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='renoCalc.contractormodel')),
                ('regions', models.ManyToManyField(to='renoCalc.regionmodel')),
                ('typeOfWork', models.ManyToManyField(to='renoCalc.propertytypemodel')),
            ],
        ),
        migrations.CreateModel(
            name='MortgageBrokerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('financeMinimum', models.IntegerField()),
                ('commission', models.JSONField()),
                ('contractor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='renoCalc.contractormodel')),
            ],
        ),
        migrations.CreateModel(
            name='LaundryAppliances',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(max_length=100)),
                ('choice', models.CharField(max_length=100)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('contractor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='renoCalc.contractormodel')),
            ],
        ),
        migrations.CreateModel(
            name='HomeInspectorModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('commission', models.JSONField()),
                ('contractor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='renoCalc.contractormodel')),
            ],
        ),
        migrations.CreateModel(
            name='ArchitectModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('commission', models.JSONField()),
                ('contractor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='renoCalc.contractormodel')),
            ],
        ),
    ]
