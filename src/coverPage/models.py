"""Models for Cover Pages"""
from django.db import models
from django.utils.translation import ugettext_lazy as _
from mezzanine.core.models import RichText
from mezzanine.pages.models import Page


class CoverPage(Page, RichText):
    """A Mezzanine page with associated cover image for top of page"""

    cover = models.ImageField(upload_to="pageCovers")

    class Meta:
        verbose_name = _("Rich Text Page with Cover Image")
        verbose_name_plural = _("Rich text pages with cover images")
