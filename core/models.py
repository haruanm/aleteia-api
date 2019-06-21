from django.db import models
from jsonfield import JSONField
from django.utils.translation import ugettext_lazy as _


class BaseModel(models.Model):
    """
    BaseModel that all other models must inherit.
    """
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name=_('updated_at'))

    class Meta:
        """
        Model meta definitions.
        """
        abstract = True


class News(BaseModel):
    date = models.DateTimeField(null=True, verbose_name=_('date'))
    title = models.CharField(max_length=255, verbose_name=_('title'))
    text = models.TextField(verbose_name=_('text'))
    url = models.URLField(max_length=2048, verbose_name=_('url'))
    is_fake = models.BooleanField(null=True, verbose_name=_('is fake?'))
    classified_at = models.DateTimeField(null=True, verbose_name=_('classified at'))

    def __str__(self):
        """
        string representation for the new
        :return: string title
        """
        return self.title

    class Meta:
        verbose_name = _('news')
        verbose_name_plural = _('news')


class ClassificationRequest(BaseModel):
    ipv4 = models.CharField(max_length=15, null=True, verbose_name=_('ipv4'))
    ipv6 = models.CharField(max_length=40, null=True, verbose_name=_('ipv6'))
    text = models.TextField(verbose_name=_('text'))
    text_date = models.DateTimeField(null=True, verbose_name=_('text_date'))
    url = models.URLField(max_length=2048, verbose_name=_('url'))
    response = JSONField(verbose_name=_('response'))

    class Meta:
        verbose_name = _('classification request')
        verbose_name_plural = _('classification requests')
