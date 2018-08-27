from django.contrib import admin
from bodies.models import Body, BodyChildRelation
from roles.models import BodyRole

class RoleInline(admin.StackedInline):
    """Show role names and links inline"""
    model = BodyRole
    fields = ('name',)
    readonly_fields = ('name',)
    template = 'role-inline.html'
    show_change_link = True

class BodyAdmin(admin.ModelAdmin):
    """Admin model for Body model."""
    inlines = [RoleInline]

admin.site.register(Body, BodyAdmin)
admin.site.register(BodyChildRelation)
