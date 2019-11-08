from django.contrib import admin
from .models import Starmap
from django.shortcuts import redirect
from .views import pdf
from django.utils.safestring import mark_safe
# Register your models here.



@admin.register(Starmap)
class StarmapAdmin(admin.ModelAdmin):
    def view_link(self):
        return mark_safe("<a href='/pdf/%d/'>View</a>" % self.id)
    list_display = ['date' ,'text', 'city', view_link]
