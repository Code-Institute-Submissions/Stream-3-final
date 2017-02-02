from django.contrib import admin
from django.contrib.flatpages.models import FlatPage
from django.contrib.flatpages.admin import FlatPageAdmin as FlatPageAdminOld
from django.contrib.flatpages.admin import FlatpageForm as FlatpageFormOld

from django.db import models
from tinymce.widgets import TinyMCE
from django import forms
from ckeditor.widgets import CKEditorWidget

# Register your models here.
class PageAdmin(FlatPageAdminOld):
    formfield_overrides = {models.TextField: {'widget': TinyMCE(attrs={'cols': 100, 'rows': 15})},}

#class FlatPageForm(FlatpageFormOld):
#    content = forms.CharField(widget=CKEditorWidget())
#    class Meta:
        #model = FlatPage
#class FlatPageAdmin(FlatPageAdminOld):
    #form = FlatpageForm

admin.site.unregister(FlatPage)
admin.site.register(FlatPage, PageAdmin)
#admin.site.register(FlatPage, FlatPageForm)
