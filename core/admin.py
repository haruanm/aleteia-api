""" This module contain the core app admin config """
from django.contrib import admin
from core.models import ClassificationRequest, News
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import Group

class ReadOnlyAdmin(admin.ModelAdmin):
    """ Base admin for read only models """
    readonly_fields = []

    def get_readonly_fields(self, request, obj=None):
        """
        Return all model fields as readonly
        :param request: django http request
        :param obj: instance managed by the admin
        :return: a list of field names
        """
        return list(self.readonly_fields) + \
            [field.name for field in obj._meta.fields] + \
            [field.name for field in obj._meta.many_to_many]


    def has_add_permission(self, request):
        """
        Method to set false to all add permisions
        :param request: django http request
        :return: boolean False
        """
        return False

    def has_delete_permission(self, request, obj=None):
        """
        Method to set false to all deletes permission
        :param request: django http request
        :param obj: instance managed by the admin
        :return: booleaan False
        """
        return False


class NewsAdmin(admin.ModelAdmin):
    """ Class do configure the admin of News """

    list_display = ('title', 'url', 'date', 'is_fake',)
    list_editable = ('is_fake',)
    ordering = ('is_fake', 'date')
    actions = ('set_as_true', 'set_as_fake',)
    list_filter = ('is_fake',)

    def set_as_fake(self, request, queryset):
        """ Set selected news as Fake

        :param request: the http request data
        :param queryset: the queryset of objects to update
        """
        queryset.update(is_fake=True)

    def set_as_true(self, request, queryset):
        """ Set selected news as True

        :param request: the http request data
        :param queryset: the queryset of objects to update
        """
        queryset.update(is_fake=False)

    set_as_fake.short_description = _("Set selected news as Fake")
    set_as_true.short_description = _("Set selected news as True")


class ClassificationRequestAdmin(ReadOnlyAdmin):
    list_display = ('url', 'created_at', 'text', 'response')


admin.site.unregister(Group)
admin.site.register(ClassificationRequest, ClassificationRequestAdmin)
admin.site.register(News, NewsAdmin)
