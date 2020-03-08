from django.contrib import admin
from .models import ContactFormTemplate
from .models import gform,form_field

admin.site.register(ContactFormTemplate)
admin.site.register(gform)
admin.site.register(form_field)
# Register your models here.
