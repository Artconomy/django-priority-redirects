from django.db import models
from django.contrib.sites.models import Site
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Redirect(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    old_path = models.CharField(_('redirect from'), max_length=200, db_index=True,
        help_text=_("This should be an absolute path, excluding the domain name. Example: '/events/search/'."))
    new_path = models.CharField(_('redirect to'), max_length=200, blank=True,
        help_text=_("This can be either an absolute path (as above) or a full URL starting with 'http://'."))
    universal = models.BooleanField(default=False, help_text="Make this affect all sites, not just the redirect's primary site.")

    class Meta:
        verbose_name = _('redirect')
        verbose_name_plural = _('redirects')
        unique_together=(('site', 'old_path'),)
        ordering = ('old_path',)

    def __str__(self):
        return "%s ---> %s" % (self.old_path, self.new_path)
