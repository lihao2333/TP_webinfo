from django.contrib import admin
from navigation.models import Section,Subsection
class SecAdmin(admin.ModelAdmin):
        list_display = ('name',)
class SubsecAdmin(admin.ModelAdmin):
        list_display = ('section','name', 'url')
admin.site.register(Section,SecAdmin)
admin.site.register(Subsection,SubsecAdmin)
