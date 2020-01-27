# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-26 21:09


from django.db import migrations, models


def created_at_to_issued_on(apps, schema_editor):
    BadgeInstance = apps.get_model('issuer', 'BadgeInstance')
    for badge in BadgeInstance.objects.all():
        badge.issued_on = badge.created_at
        badge.save()


class Migration(migrations.Migration):

    dependencies = [
        ('issuer', '0025_badgeinstance_issued_on'),
    ]

    operations = [
        migrations.RunPython(created_at_to_issued_on),
        migrations.AlterField(
            model_name='badgeinstance',
            name='issued_on',
            field=models.DateTimeField(),
        ),
    ]
