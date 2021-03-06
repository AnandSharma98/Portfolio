# Generated by Django 3.2.5 on 2021-09-21 12:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('me', '0006_rename_portfolio_designs'),
    ]

    operations = [
        migrations.CreateModel(
            name='workSample',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('link', models.URLField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='me.category')),
            ],
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
