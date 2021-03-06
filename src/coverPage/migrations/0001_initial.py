# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-16 21:33
from __future__ import unicode_literals

import django.db.models.deletion
import mezzanine.core.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [("pages", "0003_auto_20150527_1555")]

    operations = [
        migrations.CreateModel(
            name="CoverPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="pages.Page",
                    ),
                ),
                (
                    "content",
                    mezzanine.core.fields.RichTextField(
                        verbose_name="Content"
                    ),
                ),
                ("cover", models.ImageField(upload_to="pageCovers")),
            ],
            options={
                "ordering": ("_order",),
                "verbose_name_plural": "Rich text pages with cover images",
                "verbose_name": "Rich Text Page with Cover Image",
            },
            bases=("pages.page", models.Model),
        )
    ]
