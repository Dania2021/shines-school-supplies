from django.contrib import admin
from .models import Subscriber


class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'created_on')

    ordering = ('-created_on',)


admin.site.register(Subscriber, SubscriberAdmin)
