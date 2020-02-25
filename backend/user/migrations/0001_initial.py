# Generated by Django 3.0.3 on 2020-02-24 20:33

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import user.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('national_id', models.CharField(max_length=18, unique=True, verbose_name='identification')),
                ('email', models.EmailField(max_length=320, unique=True, verbose_name='email address')),
                ('birthday', models.DateField(verbose_name='birthday')),
                ('phone_number', models.CharField(max_length=15, verbose_name='phone number')),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1, verbose_name='sex')),
                ('slug', models.SlugField(blank=True, max_length=320, unique=True, verbose_name='slug')),
                ('is_athlete', models.BooleanField(default=False, verbose_name='is athlete?')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', user.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='name')),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='name')),
            ],
        ),
        migrations.AddIndex(
            model_name='state',
            index=models.Index(fields=['name'], name='state_name_idx'),
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.State', verbose_name='state'),
        ),
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='user.City', verbose_name='city'),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.AddIndex(
            model_name='city',
            index=models.Index(fields=['name'], name='city_name_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='city',
            unique_together={('name', 'state')},
        ),
    ]
