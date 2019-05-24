"""App Config for Cover Page app"""
from django.apps import AppConfig


class CoverpageConfig(AppConfig):
    """AppConfig class for CoverPage app"""

    name = "coverPage"

    def ready(self):
        """Once app is loaded, load custom settings"""
        from . import defaults  # noqa: F401
