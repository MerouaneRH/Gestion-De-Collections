from django.contrib import admin
from django.apps import apps

# Register your models here.
app = apps.get_app_config('collec_management')
for model in app.get_models():
    admin.site.register(model)
