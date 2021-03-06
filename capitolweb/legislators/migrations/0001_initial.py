# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-28 21:09
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion



states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming',
        'OL': 'Orleans',
        'DK': 'Dakota',
        'PI': 'Philippine Islands'
}


def create_states(apps, schema_editor):
    # We get the model from the versioned app registry;
    # if we directly import it, it'll be the wrong version
    State = apps.get_model("legislators", "State")
    db_alias = schema_editor.connection.alias
    state_objs = [State(name=v, short=k) for k, v in states.items()]
    State.objects.using(db_alias).bulk_create(state_objs)


def delete_states(apps, schema_editor):
    # forwards_func() creates two Country instances,
    # so reverse_func() should delete them.
    State = apps.get_model("legislators", "State")
    db_alias = schema_editor.connection.alias
    for k, v in states.items():
        State.objects.using(db_alias).filter(name=v, short=k).delete()


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CongressPerson',
            fields=[
                ('bioguide_id', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('first', models.CharField(max_length=25)),
                ('middle', models.CharField(max_length=25)),
                ('last', models.CharField(max_length=25)),
                ('suffix', models.CharField(max_length=5)),
                ('nickname', models.CharField(max_length=25)),
                ('official_full', models.CharField(max_length=50)),
                ('birthday', models.DateField(default=datetime.date(1776, 7, 4))),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('religion', models.CharField(max_length=30)),
            ],
            options={
                'ordering': ('official_full',),
            },
        ),
        migrations.CreateModel(
            name='ExternalId',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
                ('value', models.CharField(max_length=50)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='external_ids', to='legislators.CongressPerson')),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('short', models.CharField(max_length=2, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=25, unique=True)),
            ],
        ),
        migrations.RunPython(
            code=create_states,
            reverse_code=delete_states,
        ),
        migrations.CreateModel(
            name='Term',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('sen', 'Senate'), ('rep', 'House')], max_length=3)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('district', models.IntegerField(default=-1)),
                ('election_class', models.CharField(max_length=1)),
                ('state_rank', models.CharField(choices=[('junior', 'junior'), ('senior', 'Senior')], max_length=6)),
                ('party', models.CharField(max_length=25)),
                ('caucus', models.CharField(max_length=25)),
                ('address', models.TextField()),
                ('office', models.TextField()),
                ('phone', models.CharField(max_length=20, null=True)),
                ('fax', models.CharField(max_length=20, null=True)),
                ('contact_form', models.URLField(blank=True, null=True)),
                ('rss_url', models.URLField(blank=True, null=True)),
                ('url', models.URLField(blank=True, null=True)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='terms', to='legislators.CongressPerson')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='legislators.State')),],

            options={
                'ordering': ('start_date',),
            },
        ),
    ]
