# Generated by Django 3.1.3 on 2020-11-28 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20201114_1155'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='district',
            field=models.CharField(choices=[('TVM', 'Thiruvananthapuram'), ('KLM', 'Kollam'), ('PTM', 'Pathanamthitta'), ('ALP', 'Alappuzha'), ('KTM', 'Kottayam'), ('IDK', 'Idukki'), ('EKM', 'Ernakulam'), ('TSR', 'Thrissur'), ('MLP', 'Malappuram'), ('PKD', 'Palakkad'), ('MLP', 'Wayanad'), ('KZD', 'Kozhikode'), ('KNR', 'Kannur'), ('KSD', 'Kasargod')], default='EKM', max_length=30),
            preserve_default=False,
        ),
    ]
