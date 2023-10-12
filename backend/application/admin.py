from django.contrib import admin

from .models import User,Contractor,LaundryAppliances

admin.site.register(User)
admin.site.register(Contractor)
admin.site.register(LaundryAppliances)
