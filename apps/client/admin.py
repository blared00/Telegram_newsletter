from django.contrib import admin

from .models import Contact
from .tasks import create_newsletter


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'name')

    def save_model(self, request, obj, form, change):
        user_list = Contact.objects.all().values_list('email')
        user_list = [user for user in user_list]
        super().save_model(request, obj, form, change)
        create_newsletter.delay(user_list, obj.email)
