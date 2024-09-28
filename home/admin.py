from django.contrib import admin
from home.models import Contact
from home.models import Item

# Register your models here.
# By registering, models appear in the admin panel
admin.site.register(Contact)
admin.site.register(Item)