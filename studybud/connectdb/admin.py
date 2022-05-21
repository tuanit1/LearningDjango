from django.contrib import admin
from .models import User, Art

# Register your models here.
admin.site.register(Art)
admin.site.register(User)