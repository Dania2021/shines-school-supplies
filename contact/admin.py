from django.contrib import admin
from .models import ContactForm


class ContactFormAdmin(admin.ModelAdmin):

    list_display = ('contact_email', 'date')

    ordering = ('-date',)


admin.site.register(ContactForm, ContactFormAdmin)

