from django.contrib import admin
from features.models import ContactUs

@admin.register(ContactUs)
class ContactUs(admin.ModelAdmin):
    lis_display = ["name", "email",]
