"""Command to make Heroku review apps cleaner"""
from os import environ

from django.contrib.sites.models import Site
from django.core.management import BaseCommand


class Command(BaseCommand):
    """Django Management Command"""

    help = "Set or Modify the Site name and domain"

    def handle(self, *args, **options):
        """Invocation from commandline"""
        app_name = environ.get("HEROKU_APP_NAME", None)
        parent_app_name = environ.get("HEROKU_PARENT_APP_NAME", None)
        site_name = "Local Development"
        site_domain = "127.0.0.1:8000"
        if parent_app_name == "hh4r-dev":
            site_name = "HHR PR {}".format(app_name.rsplit("-", 1)[1])
            site_domain = "{}.herokuapp.com".format(app_name)
        elif app_name == "hh4r-dev":
            site_name = "HHR Development"
            site_domain = "hh4r-dev.herokuapp.com"
        elif app_name == "hh4r":
            site_name = "Hearts and Homes for Refugees"
            site_domain = "heartsandhomesforrefugees.org"
        Site.objects.update_or_create(
            pk=1, defaults={"name": site_name, "domain": site_domain}
        )
