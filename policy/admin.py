from django.contrib import admin
from .models import Policy


class PolicyAdmin(admin.ModelAdmin):
    list_display = ('premium_type', 'premium', 'cover')


admin.site.register(Policy, PolicyAdmin)
