from django.db import models
from django.utils.translation import ugettext as _

from wagtail.contrib.settings.models import BaseSetting, register_setting


@register_setting
class AnalyticsSettings(BaseSetting):
    google_analytics = models.CharField(max_length=15, help_text=_('Google Analytics tracking ID'))
