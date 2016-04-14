# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-13 20:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Metadata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trial', models.CharField(max_length=200)),
                ('Treatment', models.CharField(max_length=200)),
                ('City', models.CharField(max_length=200)),
                ('Farm', models.CharField(max_length=200)),
                ('Field', models.CharField(max_length=200)),
                ('Trial_ID', models.CharField(max_length=200)),
                ('Soil', models.CharField(max_length=200)),
                ('StationID', models.CharField(max_length=200)),
                ('Lat', models.CharField(max_length=200)),
                ('Long', models.CharField(max_length=200)),
                ('Stn_in', models.DateTimeField()),
                ('Stn_out', models.DateTimeField()),
                ('Prev_crop', models.CharField(max_length=200)),
                ('Tillage', models.CharField(max_length=200)),
                ('Season_tillage', models.CharField(max_length=200)),
                ('Plot_len', models.CharField(max_length=200)),
                ('Alley_Len', models.CharField(max_length=200)),
                ('Row_Spacing', models.CharField(max_length=200)),
                ('Planter', models.CharField(max_length=200)),
                ('Kernels_per_Plot', models.CharField(max_length=200)),
                ('grain_moisture', models.CharField(max_length=200)),
                ('Sample_Size', models.CharField(max_length=200)),
                ('LL_lat', models.CharField(max_length=200)),
                ('LL_long', models.CharField(max_length=200)),
                ('LR_lat', models.CharField(max_length=200)),
                ('LR_long', models.CharField(max_length=200)),
                ('UR_lat', models.CharField(max_length=200)),
                ('UR_long', models.CharField(max_length=200)),
                ('UL_lat', models.CharField(max_length=200)),
                ('UL_long', models.CharField(max_length=200)),
                ('Cardinal', models.CharField(max_length=200)),
                ('chk1_ped', models.CharField(max_length=200)),
                ('chk1_src', models.CharField(max_length=200)),
                ('chk2_ped', models.CharField(max_length=200)),
                ('chk2_src', models.CharField(max_length=200)),
                ('chk3_ped', models.CharField(max_length=200)),
                ('chk3_src', models.CharField(max_length=200)),
                ('chk4_ped', models.CharField(max_length=200)),
                ('chk4_src', models.CharField(max_length=200)),
                ('chk5_ped', models.CharField(max_length=200)),
                ('chk5_src', models.CharField(max_length=200)),
                ('note1', models.CharField(max_length=200)),
                ('note2', models.CharField(max_length=200)),
                ('note3', models.CharField(max_length=200)),
                ('note4', models.CharField(max_length=200)),
                ('note5', models.CharField(max_length=200)),
                ('note6', models.CharField(max_length=200)),
                ('note7', models.CharField(max_length=200)),
                ('note8', models.CharField(max_length=200)),
                ('note9', models.CharField(max_length=200)),
                ('note10', models.CharField(max_length=200)),
                ('note11', models.CharField(max_length=200)),
                ('note12', models.CharField(max_length=200)),
                ('note13', models.CharField(max_length=200)),
                ('note14', models.CharField(max_length=200)),
                ('note15', models.CharField(max_length=200)),
                ('note16', models.CharField(max_length=200)),
                ('note17', models.CharField(max_length=200)),
                ('note18', models.CharField(max_length=200)),
                ('note19', models.CharField(max_length=200)),
                ('note20', models.CharField(max_length=200)),
            ],
        ),
    ]
